from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_includes_relationship_context():
    context = AuraContext("lihat relasi")

    context.relationships = [
        {
            "person_name": "Budi",
            "relationship_type": "friend",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "[RELATIONSHIP]" in prompt
    assert "- Budi: friend" in prompt