from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_redacts_sensitive_profile_data():
    context = AuraContext(
        "Tolong bantu saya."
    )

    context.profile = "api_key=secret-profile-key"
    context.memories = []
    context.history = []

    prompt = PromptBuilder().build(context)

    assert "secret-profile-key" not in prompt
    assert "api_key=[REDACTED]" in prompt


def test_prompt_redacts_sensitive_memory_data():
    context = AuraContext(
        "Tolong bantu saya."
    )

    context.profile = None
    context.memories = [
        {
            "memory_value": "password=my-private-password"
        }
    ]
    context.history = []

    prompt = PromptBuilder().build(context)

    assert "my-private-password" not in prompt
    assert "password=[REDACTED]" in prompt


def test_prompt_redacts_sensitive_conversation_data():
    context = AuraContext(
        "Tolong bantu saya."
    )

    context.profile = None
    context.memories = []
    context.history = [
        {
            "role": "User",
            "message": "token=historical-secret",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "historical-secret" not in prompt
    assert "token=[REDACTED]" in prompt


def test_prompt_preserves_normal_context():
    context = AuraContext(
        "Tolong bantu saya."
    )

    context.profile = "AURA User"
    context.memories = [
        {
            "memory_value": "User sedang belajar Python."
        }
    ]
    context.history = []

    prompt = PromptBuilder().build(context)

    assert "AURA User" in prompt
    assert "User sedang belajar Python." in prompt