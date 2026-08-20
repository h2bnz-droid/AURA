from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_handles_empty_cognitive_model():
    context = AuraContext("Halo")

    prompt = PromptBuilder().build(context)

    assert "[PERSONAL COGNITIVE MODEL]" not in prompt
    assert "CURRENT USER MESSAGE" in prompt
    assert "Halo" in prompt