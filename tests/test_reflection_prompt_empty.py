from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_handles_empty_reflection_context():
    context = AuraContext(
        "Apa yang bisa aku pelajari?"
    )

    context.reflections = []

    prompt = PromptBuilder().build(context)

    assert "[REFLECTION]" not in prompt
