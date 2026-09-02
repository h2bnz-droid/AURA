from unittest.mock import patch

from core.context_builder import (
    build_context,
    build_integrated_cognitive_context,
    _add_cognitive_state_history_to_context,
)
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)


def test_cognitive_state_history_is_added_to_integrated_context():
    integrated_context = (
        build_integrated_cognitive_context("Halo")
    )

    cognitive_state_history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="growth",
                confidence=0.9,
                source="user_input",
            ),
            CognitiveStateHistoryItem(
                state_type="emotion",
                value="focused",
                confidence=0.8,
                source="user_input",
            ),
        ]
    )

    _add_cognitive_state_history_to_context(
        integrated_context,
        cognitive_state_history,
    )

    items = integrated_context.all_items()

    assert any(
        item.category == "mindset_history"
        and item.value == "growth"
        for item in items
    )

    assert any(
        item.category == "emotion_history"
        and item.value == "focused"
        for item in items
    )


def test_empty_cognitive_state_history_is_not_added():
    integrated_context = (
        build_integrated_cognitive_context("Halo")
    )

    cognitive_state_history = CognitiveStateHistory()

    _add_cognitive_state_history_to_context(
        integrated_context,
        cognitive_state_history,
    )

    items = integrated_context.all_items()

    assert not any(
        item.category.endswith("_history")
        for item in items
    )

@patch("core.context_builder.cognitive_state_service")
def test_build_context_adds_cognitive_state_history_to_integrated_context(
    mock_cognitive_state_service,
):
    mock_cognitive_state_service.latest.return_value = None

    mock_cognitive_state_service.history_context.return_value = (
        CognitiveStateHistory(
            items=[
                CognitiveStateHistoryItem(
                    state_type="mindset",
                    value="resilient",
                    confidence=0.9,
                    source="user_message",
                )
            ]
        )
    )

    context = build_context("Halo")

    items = context.integrated_cognitive_context.all_items()

    assert any(
        item.category == "mindset_history"
        and item.value == "resilient"
        for item in items
    )