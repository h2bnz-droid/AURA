from unittest.mock import patch

from services.temporal_service import (
    record_event,
    event_history,
    latest_event,
    calculate_trend,
)


@patch("services.temporal_service.save_event")
def test_record_event(mock_save):
    record_event(
        "learning",
        "Python",
        "50",
    )

    mock_save.assert_called_once_with(
        "learning",
        "Python",
        "50",
        None,
    )


@patch("services.temporal_service.get_history")
def test_event_history(mock_history):
    mock_history.return_value = [
        {
            "event_type": "learning",
            "subject": "Python",
            "value": "50",
        }
    ]

    result = event_history(
        event_type="learning",
        subject="Python",
    )

    mock_history.assert_called_once_with(
        event_type="learning",
        subject="Python",
    )

    assert result[0]["value"] == "50"


@patch("services.temporal_service.get_latest")
def test_latest_event(mock_latest):
    mock_latest.return_value = {
        "event_type": "emotion",
        "subject": "current",
        "value": "happy",
    }

    result = latest_event(
        "emotion",
        "current",
    )

    mock_latest.assert_called_once_with(
        "emotion",
        "current",
    )

    assert result["value"] == "happy"


def test_calculate_trend_increasing():
    assert calculate_trend(
        [20, 40, 60]
    ) == "increasing"


def test_calculate_trend_decreasing():
    assert calculate_trend(
        [80, 50, 20]
    ) == "decreasing"


def test_calculate_trend_stable():
    assert calculate_trend(
        [50, 50, 50]
    ) == "stable"


def test_calculate_trend_with_insufficient_data():
    assert calculate_trend(
        [50]
    ) == "stable"