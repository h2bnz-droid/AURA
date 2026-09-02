from core.context_builder import build_context
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)


def test_build_context_includes_cognitive_state_history(
    monkeypatch,
):
    expected = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="growth",
                confidence=0.9,
                source="user_input",
            )
        ]
    )

    monkeypatch.setattr(
        "core.context_builder.cognitive_state_service.history_context",
        lambda: expected,
    )

    context = build_context("Halo")

    assert context.cognitive_state_history == expected


def test_build_context_handles_empty_cognitive_state_history(
    monkeypatch,
):
    expected = CognitiveStateHistory()

    monkeypatch.setattr(
        "core.context_builder.cognitive_state_service.history_context",
        lambda: expected,
    )

    context = build_context("Halo")

    assert context.cognitive_state_history == expected
    assert context.cognitive_state_history.items == []