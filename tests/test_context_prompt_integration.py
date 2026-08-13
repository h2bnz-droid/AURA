from unittest.mock import patch

from core.chat import ask
from core.context import AuraContext


@patch("core.chat.chat")
@patch("core.chat.build_context")
@patch("core.chat.add")
def test_context_flows_into_ai_prompt(
    mock_add,
    mock_build_context,
    mock_chat,
):
    context = AuraContext("Apa yang sedang aku kerjakan?")

    context.profile = "Hibban"

    context.memories = [
        {
            "memory_value": "User sedang membangun AURA"
        },
        {
            "memory_value": "User sedang mengerjakan Sprint 3"
        },
    ]

    context.history = [
        {
            "role": "User",
            "message": "Kita sudah menyelesaikan Sprint 2."
        },
        {
            "role": "AURA",
            "message": "Sekarang kita masuk Sprint 3."
        },
    ]

    mock_build_context.return_value = context
    mock_chat.return_value = "Kamu sedang mengerjakan Sprint 3."

    result = ask("Apa yang sedang aku kerjakan?")

    assert result == "Kamu sedang mengerjakan Sprint 3."

    mock_build_context.assert_called_once_with(
        "Apa yang sedang aku kerjakan?"
    )

    mock_chat.assert_called_once()

    messages = mock_chat.call_args.args[0]

    assert len(messages) == 2

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "user"

    prompt = messages[1]["content"]

    assert "Hibban" in prompt

    assert "User sedang membangun AURA" in prompt
    assert "User sedang mengerjakan Sprint 3" in prompt

    assert "Kita sudah menyelesaikan Sprint 2." in prompt
    assert "Sekarang kita masuk Sprint 3." in prompt

    assert "Apa yang sedang aku kerjakan?" in prompt


@patch("core.chat.chat")
@patch("core.chat.build_context")
@patch("core.chat.add")
def test_chat_persists_user_and_ai_messages(
    mock_add,
    mock_build_context,
    mock_chat,
):
    context = AuraContext("Halo AURA")

    mock_build_context.return_value = context
    mock_chat.return_value = "Halo juga!"

    result = ask("Halo AURA")

    assert result == "Halo juga!"

    assert mock_add.call_count == 2

    mock_add.assert_any_call(
        "User",
        "Halo AURA",
    )

    mock_add.assert_any_call(
        "AURA",
        "Halo juga!",
    )
