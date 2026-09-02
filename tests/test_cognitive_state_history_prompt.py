from core.context import AuraContext
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)
from core.context_builder import (
    build_integrated_cognitive_context,
    _add_cognitive_state_history_to_context,
)
from core.prompt_builder import PromptBuilder


def test_cognitive_state_history_appears_in_prompt():
    context = AuraContext("Halo")

    integrated_context = (
        build_integrated_cognitive_context("Halo")
    )

    cognitive_state_history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="resilient",
                confidence=0.9,
                source="user_message",
            ),
            CognitiveStateHistoryItem(
                state_type="emotion",
                value="focused",
                confidence=0.8,
                source="user_message",
            ),
        ]
    )

    _add_cognitive_state_history_to_context(
        integrated_context,
        cognitive_state_history,
    )

    context.integrated_cognitive_context = integrated_context

    prompt = PromptBuilder().build(context)

    assert "- mindset_history: resilient" in prompt
    assert "- emotion_history: focused" in prompt