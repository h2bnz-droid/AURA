from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emotion TEXT NOT NULL,
            intensity REAL NOT NULL DEFAULT 0.0,
            source TEXT NOT NULL DEFAULT 'user_message',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_emotion(
    emotion: str,
    intensity: float = 0.0,
    source: str = "user_message",
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emotions (emotion, intensity, source)
        VALUES (?, ?, ?)
    """, (emotion, intensity, source))

    conn.commit()
    conn.close()


def get_latest_emotion():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, emotion, intensity, source, created_at
        FROM emotions
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return {
        "id": row["id"],
        "emotion": row["emotion"],
        "intensity": row["intensity"],
        "source": row["source"],
        "created_at": row["created_at"],
    }


def get_emotion_history(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, emotion, intensity, source, created_at
        FROM emotions
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return [
        {
            "id": row["id"],
            "emotion": row["emotion"],
            "intensity": row["intensity"],
            "source": row["source"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]