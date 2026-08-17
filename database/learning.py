from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'active',
            progress INTEGER NOT NULL DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def create_learning(topic: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO learning (topic, status, progress)
        VALUES (?, 'active', 0)
    """, (topic,))

    conn.commit()
    conn.close()


def get_active_learning():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, topic, status, progress, created_at, updated_at
        FROM learning
        WHERE status = 'active'
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "topic": row[1],
            "status": row[2],
            "progress": row[3],
            "created_at": row[4],
            "updated_at": row[5],
        }
        for row in rows
    ]


def update_progress(topic: str, progress: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE learning
        SET progress = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE topic = ?
          AND status = 'active'
    """, (progress, topic))

    conn.commit()
    conn.close()