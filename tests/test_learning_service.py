from unittest.mock import patch

from services.learning_service import (
    start_learning,
    active_learning,
    update_learning_progress,
    find_learning,
)


@patch("services.learning_service.create_learning")
def test_start_learning(mock_create):
    start_learning("Python")

    mock_create.assert_called_once()

    args = mock_create.call_args.args

    assert args[0] == "Python"


@patch("services.learning_service.get_active_learning")
def test_active_learning(mock_get):
    expected = [
        {
            "topic": "Python",
            "progress": 40,
            "status": "active",
        }
    ]

    mock_get.return_value = expected

    result = active_learning()

    assert result == expected


@patch("services.learning_service.update_progress")
def test_update_learning_progress(mock_update):
    update_learning_progress("Python", 50)

    mock_update.assert_called_once_with(
        "Python",
        50,
    )


@patch("services.learning_service.get_active_learning")
def test_find_learning(mock_get):
    mock_get.return_value = [
        {
            "topic": "Python",
            "progress": 40,
            "status": "active",
        },
        {
            "topic": "Matematika",
            "progress": 20,
            "status": "active",
        },
    ]

    result = find_learning("python")

    assert result["topic"] == "Python"