from core.context import AuraContext
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)
from core.prompt_builder import PromptBuilder


def test_prompt_includes_integrated_cognitive_context():
    context = AuraContext("Apa yang kamu tahu tentang saya?")

    context.integrated_cognitive_context = IntegratedCognitiveContext(
        stable=[
            CognitiveContextItem(
                category="skill",
                value="Python",
                source="user_statement",
                confidence=1.0,
                relevance=1.0,
            )
        ],
        relevant=[
            CognitiveContextItem(
                category="goal",
                value="Build AURA",
                source="goal",
                confidence=1.0,
                relevance=1.0,
            )
        ],
    )

    prompt = PromptBuilder().build(context)

    assert "[INTEGRATED COGNITIVE CONTEXT]" in prompt
    assert "Python" in prompt
    assert "Build AURA" in prompt


def test_prompt_handles_empty_integrated_cognitive_context():
    context = AuraContext("Halo")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext()
    )

    prompt = PromptBuilder().build(context)

    assert "[INTEGRATED COGNITIVE CONTEXT]" not in prompt
    assert "CURRENT USER MESSAGE" in prompt
    assert "Halo" in prompt