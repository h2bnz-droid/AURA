from core.context import AuraContext
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)
from core.prompt_builder import PromptBuilder


def test_integrated_cognitive_context_flows_into_prompt():
    context = AuraContext(
        "Apa yang kamu tahu tentang saya?"
    )

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
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
                    relevance=0.9,
                )
            ],
            recent=[
                CognitiveContextItem(
                    category="reflection",
                    value="Sprint 011",
                    source="reflection",
                    confidence=1.0,
                    relevance=0.8,
                )
            ],
        )
    )

    prompt = PromptBuilder().build(context)

    assert "[INTEGRATED COGNITIVE CONTEXT]" in prompt
    assert "skill: Python" in prompt
    assert "goal: Build AURA" in prompt
    assert "reflection: Sprint 011" in prompt

    assert "CURRENT USER MESSAGE" in prompt
    assert "Apa yang kamu tahu tentang saya?" in prompt


def test_integrated_context_preserves_layer_order():
    context = AuraContext("test")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext(
            stable=[
                CognitiveContextItem(
                    category="identity",
                    value="developer",
                    source="user_statement",
                    confidence=1.0,
                )
            ],
            relevant=[
                CognitiveContextItem(
                    category="goal",
                    value="Build AURA",
                    source="goal",
                    confidence=1.0,
                )
            ],
            recent=[
                CognitiveContextItem(
                    category="reflection",
                    value="Sprint 011",
                    source="reflection",
                    confidence=1.0,
                )
            ],
        )
    )

    prompt = PromptBuilder().build(context)

    stable_index = prompt.index("identity: developer")
    relevant_index = prompt.index("goal: Build AURA")
    recent_index = prompt.index("reflection: Sprint 011")

    assert stable_index < relevant_index
    assert relevant_index < recent_index


def test_empty_integrated_context_does_not_break_pipeline():
    context = AuraContext("Halo")

    context.integrated_cognitive_context = (
        IntegratedCognitiveContext()
    )

    prompt = PromptBuilder().build(context)

    assert "[INTEGRATED COGNITIVE CONTEXT]" not in prompt
    assert "CURRENT USER MESSAGE" in prompt
    assert "Halo" in prompt