from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cognitive_states (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state_type TEXT NOT NULL,
            value TEXT NOT NULL,
            confidence REAL NOT NULL DEFAULT 0.0,
            source TEXT NOT NULL DEFAULT 'system',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_state(
    state_type: str,
    value: str,
    confidence: float = 0.0,
    source: str = "system",
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cognitive_states (
            state_type,
            value,
            confidence,
            source
        )
        VALUES (?, ?, ?, ?)
    """, (
        state_type,
        value,
        confidence,
        source,
    ))

    conn.commit()
    conn.close()


def get_latest_state(state_type: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            state_type,
            value,
            confidence,
            source,
            created_at,
            updated_at
        FROM cognitive_states
        WHERE state_type = ?
        ORDER BY id DESC
        LIMIT 1
    """, (state_type,))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row["id"],
        "state_type": row["state_type"],
        "value": row["value"],
        "confidence": row["confidence"],
        "source": row["source"],
        "created_at": row["created_at"],
        "updated_at": row["updated_at"],
    }


def get_state_history(
    state_type: str | None = None,
    limit: int = 10,
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            id,
            state_type,
            value,
            confidence,
            source,
            created_at,
            updated_at
        FROM cognitive_states
    """

    params = []

    if state_type is not None:
        query += " WHERE state_type = ?"
        params.append(state_type)

    query += " ORDER BY id DESC LIMIT ?"
    params.append(limit)

    cursor.execute(query, params)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "state_type": row["state_type"],
            "value": row["value"],
            "confidence": row["confidence"],
            "source": row["source"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],
        }
        for row in rows
    ]