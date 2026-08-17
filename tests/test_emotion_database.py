from database.connection import get_connection
from database.emotions import (
    create_table,
    save_emotion,
    get_latest_emotion,
    get_emotion_history,
)


def test_emotion_table_exists():
    create_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
          AND name = 'emotions'
    """)

    row = cursor.fetchone()
    conn.close()

    assert row is not None


def test_save_and_get_latest_emotion():
    create_table()

    save_emotion(
        "happy",
        0.8,
        "user_message",
    )

    emotion = get_latest_emotion()

    assert emotion is not None
    assert emotion["emotion"] == "happy"
    assert emotion["intensity"] == 0.8


def test_get_emotion_history():
    create_table()

    save_emotion("sad", 0.5)
    save_emotion("excited", 0.9)

    history = get_emotion_history()

    assert len(history) >= 2
    assert history[0]["emotion"] == "excited"