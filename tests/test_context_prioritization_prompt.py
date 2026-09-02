from core.context import AuraContext
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)
from core.prompt_builder import PromptBuilder


def test_prompt_prioritizes_integrated_cognitive_context():
    context = AuraContext("Halo")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
            stable=[
                CognitiveContextItem(
                    category="memory",
                    value="User suka Python",
                    source="memory_service",
                    confidence=1.0,
                )
            ],
            relevant=[
                CognitiveContextItem(
                    category="mindset",
                    value="growth",
                    source="mindset_service",
                    confidence=1.0,
                )
            ],
            recent=[
                CognitiveContextItem(
                    category="emotion",
                    value="focused",
                    source="cognitive_state",
                    confidence=1.0,
                )
            ],
        )
    )

    prompt = PromptBuilder().build(context)

    mindset_position = prompt.index(
        "- mindset: growth"
    )

    emotion_position = prompt.index(
        "- emotion: focused"
    )

    memory_position = prompt.index(
        "- memory: User suka Python"
    )

    assert mindset_position < emotion_position
    assert emotion_position < memory_position


def test_prompt_removes_duplicate_integrated_context():
    context = AuraContext("Halo")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
            stable=[
                CognitiveContextItem(
                    category="memory",
                    value="User suka Python",
                    source="memory_service",
                    confidence=1.0,
                )
            ],
            relevant=[
                CognitiveContextItem(
                    category="memory",
                    value="User suka Python",
                    source="memory_service",
                    confidence=1.0,
                )
            ],
        )
    )

    prompt = PromptBuilder().build(context)

    assert prompt.count(
        "- memory: User suka Python"
    ) == 1

def test_prompt_applies_integrated_context_default_limit():
    context = AuraContext("Halo")

    items = [
        CognitiveContextItem(
            category="memory",
            value=f"Memory {index}",
            source="memory_service",
            confidence=1.0,
        )
        for index in range(15)
    ]

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
            stable=items
        )
    )

    prompt = PromptBuilder().build(context)

    memory_lines = [
        line
        for line in prompt.splitlines()
        if line.startswith("- memory:")
    ]

    assert len(memory_lines) == 10

def test_prompt_handles_empty_integrated_cognitive_context():
    context = AuraContext("Halo")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext()
    )

    prompt = PromptBuilder().build(context)

    assert "[INTEGRATED COGNITIVE CONTEXT]" not in prompt

def test_prompt_keeps_all_items_below_default_limit():
    context = AuraContext("Halo")

    items = [
        CognitiveContextItem(
            category="memory",
            value=f"Memory {index}",
            source="memory_service",
            confidence=1.0,
        )
        for index in range(5)
    ]

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
            stable=items
        )
    )

    prompt = PromptBuilder().build(context)

    memory_lines = [
        line
        for line in prompt.splitlines()
        if line.startswith("- memory:")
    ]

    assert len(memory_lines) == 5