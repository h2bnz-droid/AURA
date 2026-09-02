from core.context import AuraContext
from core.domain.cognitive_state import CognitiveState
from core.prompt_builder import PromptBuilder


def test_prompt_includes_cognitive_state():
    context = AuraContext("Halo")

    context.cognitive_state = CognitiveState(
        mindset="focused",
        emotion="calm",
        source="system",
    )

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE STATE]" in prompt
    assert "- Mindset: focused" in prompt
    assert "- Emotion: calm" in prompt
    assert "- Source: system" in prompt


def test_prompt_handles_empty_cognitive_state():
    context = AuraContext("Halo")

    context.cognitive_state = CognitiveState()

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE STATE]" in prompt
    assert "- Source: system" in prompt


def test_prompt_omits_empty_cognitive_state_values():
    context = AuraContext("Halo")

    context.cognitive_state = CognitiveState(
        mindset=None,
        emotion=None,
        source="system",
    )

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE STATE]" in prompt
    assert "- Mindset:" not in prompt
    assert "- Emotion:" not in prompt