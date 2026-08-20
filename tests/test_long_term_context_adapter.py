from services.long_term_context_service import _get_value


def test_get_value_from_dict():
    row = {
        "title": "Build AURA",
        "progress": 50,
    }

    assert _get_value(row, "title", 1) == "Build AURA"
    assert _get_value(row, "progress", 2) == 50


def test_get_value_from_sqlite_row():
    import sqlite3

    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE goals (
            id INTEGER,
            title TEXT,
            progress INTEGER
        )
        """
    )

    cursor.execute(
        """
        INSERT INTO goals VALUES (1, 'Build AURA', 50)
        """
    )

    row = cursor.execute(
        "SELECT * FROM goals"
    ).fetchone()

    assert _get_value(row, "title", 1) == "Build AURA"
    assert _get_value(row, "progress", 2) == 50

    connection.close()