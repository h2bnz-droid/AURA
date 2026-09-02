from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_includes_cognitive_behavior():

    context = AuraContext("Aku merasa khawatir.")

    context.cognitive_behavior = (
        "Gunakan nada yang menenangkan."
    )

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE BEHAVIOR]" in prompt

    assert (
        "Gunakan nada yang menenangkan."
        in prompt
    )


def test_prompt_handles_empty_cognitive_behavior():

    context = AuraContext("Halo")

    context.cognitive_behavior = None

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE BEHAVIOR]" not in prompt