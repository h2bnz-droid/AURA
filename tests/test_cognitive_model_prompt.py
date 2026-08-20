from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_contains_cognitive_model():
    context = AuraContext("Apa yang kamu tahu tentang saya?")

    context.cognitive_model = [
        {
            "attribute_name": "skill",
            "attribute_value": "Python",
            "category": "skill",
            "source": "user_statement",
            "confidence": 1.0,
            "created_at": "2026-08-20T00:00:00",
            "updated_at": "2026-08-20T00:00:00",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "[PERSONAL COGNITIVE MODEL]" in prompt
    assert "skill: Python" in prompt