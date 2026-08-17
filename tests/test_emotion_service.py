from unittest.mock import patch

from services.emotion_service import (
    emotion_history,
    find_emotion,
    latest_emotion,
    record_emotion,
)


@patch("services.emotion_service.save_emotion")
def test_record_emotion(mock_save):
    record_emotion("happy", 0.8)

    mock_save.assert_called_once_with(
        "happy",
        0.8,
        "user_message",
    )


@patch("services.emotion_service.get_latest_emotion")
def test_latest_emotion(mock_latest):
    mock_latest.return_value = {
        "emotion": "sad",
        "intensity": 0.5,
    }

    result = latest_emotion()

    assert result["emotion"] == "sad"
    mock_latest.assert_called_once()


@patch("services.emotion_service.get_emotion_history")
def test_emotion_history(mock_history):
    mock_history.return_value = []

    result = emotion_history(5)

    assert result == []
    mock_history.assert_called_once_with(5)


@patch("services.emotion_service.get_emotion_history")
def test_find_emotion(mock_history):
    mock_history.return_value = [
        {
            "emotion": "happy",
            "intensity": 0.8,
        },
        {
            "emotion": "sad",
            "intensity": 0.4,
        },
    ]

    result = find_emotion(" HAPPY ")

    assert result["emotion"] == "happy"