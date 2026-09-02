from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)


def test_cognitive_state_history_starts_empty():
    history = CognitiveStateHistory()

    assert history.items == []


def test_cognitive_state_history_latest_returns_latest_item():
    first = CognitiveStateHistoryItem(
        state_type="mindset",
        value="growth",
        confidence=0.8,
        source="user_input",
    )

    second = CognitiveStateHistoryItem(
        state_type="emotion",
        value="focused",
        confidence=0.9,
        source="user_input",
    )

    history = CognitiveStateHistory(
        items=[
            second,
            first,
        ]
    )

    assert history.latest() == second


def test_cognitive_state_history_latest_returns_none_when_empty():
    history = CognitiveStateHistory()

    assert history.latest() is None


def test_cognitive_state_history_filters_by_state_type():
    mindset = CognitiveStateHistoryItem(
        state_type="mindset",
        value="growth",
        confidence=0.8,
        source="user_input",
    )

    emotion = CognitiveStateHistoryItem(
        state_type="emotion",
        value="focused",
        confidence=0.9,
        source="user_input",
    )

    history = CognitiveStateHistory(
        items=[
            mindset,
            emotion,
        ]
    )

    result = history.filter_by_type("mindset")

    assert result == [mindset]