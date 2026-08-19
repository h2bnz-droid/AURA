from unittest.mock import patch

from services.reflection_service import save, latest, all


@patch("services.reflection_service.create_reflection")
def test_reflection_service_save(mock_create):
    save(
        "Summary",
        "Insights",
        "Questions",
    )

    mock_create.assert_called_once()


@patch("services.reflection_service.get_latest_reflections")
def test_reflection_service_latest(mock_latest):
    mock_latest.return_value = [
        ("reflection",)
    ]

    result = latest()

    mock_latest.assert_called_once_with(5)
    assert result == [("reflection",)]


@patch("services.reflection_service.get_all_reflections")
def test_reflection_service_all(mock_all):
    mock_all.return_value = [
        ("reflection",)
    ]

    result = all()

    mock_all.assert_called_once()
    assert result == [("reflection",)]