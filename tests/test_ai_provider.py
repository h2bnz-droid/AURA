import pytest

from core.ai_provider import AIProviderError, chat
from core.ai_provider import _sanitize_messages


def test_provider_error_returns_fallback(monkeypatch):
    def failing_chat(**kwargs):
        raise RuntimeError("connection failed")

    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        failing_chat,
    )

    result = chat(
        [
            {
                "role": "user",
                "content": "hello",
            }
        ]
    )

    assert result
    assert "ollama" not in result.lower()
    assert "exception" not in result.lower()
    assert "traceback" not in result.lower()


def test_invalid_response_type_is_rejected(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: "invalid",
    )

    with pytest.raises(AIProviderError):
        chat([])


def test_missing_message_is_rejected(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: {},
    )

    with pytest.raises(AIProviderError):
        chat([])


def test_invalid_message_type_is_rejected(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: {"message": "invalid"},
    )

    with pytest.raises(AIProviderError):
        chat([])


def test_missing_content_is_rejected(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: {"message": {}},
    )

    with pytest.raises(AIProviderError):
        chat([])


def test_empty_content_is_rejected(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: {"message": {"content": "   "}},
    )

    with pytest.raises(AIProviderError):
        chat([])


def test_valid_response_returns_content(monkeypatch):
    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        lambda **kwargs: {
            "message": {
                "content": "Halo, saya AURA.",
            }
        },
    )

    result = chat([])

    assert result == "Halo, saya AURA."


def test_sanitize_messages_redacts_sensitive_content():
    messages = [
        {
            "role": "user",
            "content": "api_key=super-secret-key",
        }
    ]

    result = _sanitize_messages(messages)

    assert result[0]["content"] == (
        "api_key=[REDACTED]"
    )


def test_sanitize_messages_preserves_message_structure():
    messages = [
        {
            "role": "system",
            "content": "AURA system prompt",
        },
        {
            "role": "user",
            "content": "Saya sedang belajar Python.",
        },
    ]

    result = _sanitize_messages(messages)

    assert result == messages


def test_sanitize_messages_does_not_mutate_original_messages():
    messages = [
        {
            "role": "user",
            "content": "password=original-secret",
        }
    ]

    original_content = messages[0]["content"]

    _sanitize_messages(messages)

    assert messages[0]["content"] == original_content


def test_sanitize_messages_rejects_invalid_messages():
    try:
        _sanitize_messages("invalid messages")
    except Exception as exc:
        assert type(exc).__name__ == "AIProviderError"
    else:
        raise AssertionError(
            "Expected AIProviderError"
        )

def test_chat_returns_fallback_when_provider_fails(monkeypatch):
    from core.ai_provider import chat

    def failing_chat(**kwargs):
        raise RuntimeError("provider unavailable")

    monkeypatch.setattr(
        "core.ai_provider.ollama.chat",
        failing_chat,
    )

    result = chat(
        [
            {
                "role": "user",
                "content": "hello",
            }
        ]
    )

    assert result
    assert "ollama" not in result.lower()
    assert "exception" not in result.lower()