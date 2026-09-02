from unittest.mock import patch

from core.domain.cognitive_state import CognitiveState
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
)
from services.cognitive_state_service import CognitiveStateService


@patch("services.cognitive_state_service.create_table")
def test_initialize_creates_table(mock_create_table):
    service = CognitiveStateService()

    service.initialize()

    mock_create_table.assert_called_once()


@patch("services.cognitive_state_service.save_state")
def test_record_mindset_saves_and_returns_cognitive_state(
    mock_save_state,
):
    service = CognitiveStateService()

    result = service.record_mindset(
        mindset="resilient",
        confidence=0.9,
        source="user_message",
    )

    assert isinstance(result, CognitiveState)
    assert result.mindset == "resilient"
    assert result.emotion is None
    assert result.source == "user_message"

    mock_save_state.assert_called_once_with(
        state_type="mindset",
        value="resilient",
        confidence=0.9,
        source="user_message",
    )


@patch("services.cognitive_state_service.save_state")
def test_record_emotion_saves_and_returns_cognitive_state(
    mock_save_state,
):
    service = CognitiveStateService()

    result = service.record_emotion(
        emotion="frustrated",
        confidence=0.8,
        source="user_message",
    )

    assert isinstance(result, CognitiveState)
    assert result.mindset is None
    assert result.emotion == "frustrated"
    assert result.source == "user_message"

    mock_save_state.assert_called_once_with(
        state_type="emotion",
        value="frustrated",
        confidence=0.8,
        source="user_message",
    )


@patch("services.cognitive_state_service.get_latest_state")
def test_latest_returns_empty_cognitive_state_when_no_data(
    mock_get_latest_state,
):
    mock_get_latest_state.return_value = None

    service = CognitiveStateService()

    result = service.latest()

    assert isinstance(result, CognitiveState)
    assert result.mindset is None
    assert result.emotion is None
    assert result.source == "system"

    assert mock_get_latest_state.call_count == 2


@patch("services.cognitive_state_service.get_latest_state")
def test_latest_returns_combined_cognitive_state(
    mock_get_latest_state,
):
    mock_get_latest_state.side_effect = [
        {
            "state_type": "mindset",
            "value": "resilient",
            "confidence": 0.9,
            "source": "user_message",
        },
        {
            "state_type": "emotion",
            "value": "frustrated",
            "confidence": 0.8,
            "source": "user_message",
        },
    ]

    service = CognitiveStateService()

    result = service.latest()

    assert isinstance(result, CognitiveState)
    assert result.mindset == "resilient"
    assert result.emotion == "frustrated"
    assert result.source == "user_message"

    mock_get_latest_state.assert_any_call("mindset")
    mock_get_latest_state.assert_any_call("emotion")


@patch("services.cognitive_state_service.get_state_history")
def test_history_returns_database_state_history(
    mock_get_state_history,
):
    expected = [
        {
            "state_type": "mindset",
            "value": "resilient",
            "confidence": 0.9,
            "source": "user_message",
        }
    ]

    mock_get_state_history.return_value = expected

    service = CognitiveStateService()

    result = service.history(
        state_type="mindset",
        limit=5,
    )

    assert result == expected

    mock_get_state_history.assert_called_once_with(
        state_type="mindset",
        limit=5,
    )

@patch("services.cognitive_state_service.get_state_history")
def test_history_context_returns_cognitive_state_history(
    mock_get_state_history,
):
    mock_get_state_history.return_value = [
        {
            "state_type": "mindset",
            "value": "growth",
            "confidence": 0.9,
            "source": "user_input",
            "created_at": "2026-09-02",
        }
    ]

    service = CognitiveStateService()

    result = service.history_context()

    assert isinstance(result, CognitiveStateHistory)
    assert len(result.items) == 1

    item = result.items[0]

    assert item.state_type == "mindset"
    assert item.value == "growth"
    assert item.confidence == 0.9
    assert item.source == "user_input"
    assert item.created_at == "2026-09-02"

    mock_get_state_history.assert_called_once_with(
        state_type=None,
        limit=10,
    )