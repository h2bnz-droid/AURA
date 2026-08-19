from unittest.mock import patch

from database.reflections import (
    create_reflection,
    get_latest_reflections,
    get_all_reflections,
)


@patch("database.reflections.get_connection")
def test_create_reflection(mock_connection):
    conn = mock_connection.return_value
    cursor = conn.cursor.return_value

    create_reflection(
        "Summary",
        "Insights",
        "Questions",
        "2026-08-19 09:00:00",
    )

    cursor.execute.assert_called_once()
    conn.commit.assert_called_once()
    conn.close.assert_called_once()


@patch("database.reflections.get_connection")
def test_get_latest_reflections(mock_connection):
    conn = mock_connection.return_value
    cursor = conn.cursor.return_value
    cursor.fetchall.return_value = [("reflection",)]

    result = get_latest_reflections(5)

    assert result == [("reflection",)]
    cursor.execute.assert_called_once()
    conn.close.assert_called_once()


@patch("database.reflections.get_connection")
def test_get_all_reflections(mock_connection):
    conn = mock_connection.return_value
    cursor = conn.cursor.return_value
    cursor.fetchall.return_value = [("reflection",)]

    result = get_all_reflections()

    assert result == [("reflection",)]
    cursor.execute.assert_called_once()
    conn.close.assert_called_once()
