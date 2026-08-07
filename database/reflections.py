from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reflections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summary TEXT NOT NULL,
        insights TEXT NOT NULL,
        questions TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def create_reflection(
    summary: str,
    insights: str,
    questions: str,
    created_at: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reflections (
            summary,
            insights,
            questions,
            created_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        summary,
        insights,
        questions,
        created_at,
    ))

    conn.commit()
    conn.close()


def get_latest_reflections(limit: int = 5):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM reflections
        ORDER BY created_at DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_all_reflections():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM reflections
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows