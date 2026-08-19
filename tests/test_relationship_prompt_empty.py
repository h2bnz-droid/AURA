from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_handles_empty_relationship_context():
    context = AuraContext("halo")
    context.relationships = []

    prompt = PromptBuilder().build(context)

    assert "[RELATIONSHIP]" not in prompt