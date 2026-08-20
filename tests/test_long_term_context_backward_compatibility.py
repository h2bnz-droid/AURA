from unittest.mock import patch

from core.context_builder import build_context
from core.prompt_builder import PromptBuilder


@patch("core.context_builder.collect_long_term_context")
def test_long_term_context_does_not_break_existing_context(
    mock_collect_long_term_context,
):
    mock_collect_long_term_context.return_value = [
        {
            "content": "Software Engineer",
            "category": "aspiration",
            "source": "personal_cognitive_model",
        }
    ]

    context = build_context("Bagaimana perkembangan AURA?")

    context.profile = "AURA User"

    context.memories = [
        {
            "memory_value": "User sedang membangun AURA",
        }
    ]

    context.history = [
        {
            "role": "user",
            "message": "Aku ingin AURA menjadi AI companion.",
        }
    ]

    context.relationships = [
        {
            "person_name": "Budi",
            "relationship_type": "friend",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "AURA User" in prompt
    assert "User sedang membangun AURA" in prompt
    assert "Aku ingin AURA menjadi AI companion." in prompt
    assert "Budi" in prompt
    assert "Software Engineer" in prompt