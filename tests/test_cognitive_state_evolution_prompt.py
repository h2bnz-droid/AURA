from core.context import AuraContext
from core.domain.cognitive_state_evolution import (
    CognitiveStateEvolution,
)
from core.prompt_builder import PromptBuilder


def test_prompt_contains_cognitive_state_evolution():

    context = AuraContext("test")

    context.cognitive_state_evolution = [
        CognitiveStateEvolution(
            state_type="mindset",
            previous_value="growth",
            current_value="resilient",
            status="transition",
        )
    ]

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE STATE EVOLUTION]" in prompt
    assert "mindset: transition" in prompt


def test_prompt_contains_emotion_evolution():

    context = AuraContext("test")

    context.cognitive_state_evolution = [
        CognitiveStateEvolution(
            state_type="emotion",
            previous_value="frustrated",
            current_value="focused",
            status="transition",
        )
    ]

    prompt = PromptBuilder().build(context)

    assert "emotion: transition" in prompt


def test_unknown_evolution_not_in_prompt():

    context = AuraContext("test")

    context.cognitive_state_evolution = [
        CognitiveStateEvolution(
            state_type="mindset",
            status="unknown",
        )
    ]

    prompt = PromptBuilder().build(context)

    assert "[COGNITIVE STATE EVOLUTION]" not in prompt
    assert "mindset: unknown" not in prompt


def test_empty_evolution_does_not_break_prompt():

    context = AuraContext("test")

    context.cognitive_state_evolution = []

    prompt = PromptBuilder().build(context)

    assert "CURRENT USER MESSAGE" in prompt
    assert "test" in prompt