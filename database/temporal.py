from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS temporal_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_type TEXT NOT NULL,
            subject TEXT NOT NULL,
            value TEXT,
            metadata TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_event(
    event_type: str,
    subject: str,
    value: str | None = None,
    metadata: str | None = None,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO temporal_events (
            event_type,
            subject,
            value,
            metadata
        )
        VALUES (?, ?, ?, ?)
    """, (
        event_type,
        subject,
        value,
        metadata,
    ))

    conn.commit()
    conn.close()


def get_history(
    event_type: str | None = None,
    subject: str | None = None,
):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT
            id,
            event_type,
            subject,
            value,
            metadata,
            created_at
        FROM temporal_events
        WHERE 1 = 1
    """

    params = []

    if event_type is not None:
        query += " AND event_type = ?"
        params.append(event_type)

    if subject is not None:
        query += " AND subject = ?"
        params.append(subject)

    query += " ORDER BY id ASC"

    cursor.execute(query, params)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row["id"],
            "event_type": row["event_type"],
            "subject": row["subject"],
            "value": row["value"],
            "metadata": row["metadata"],
            "created_at": row["created_at"],
        }
        for row in rows
    ]


def get_latest(
    event_type: str,
    subject: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            event_type,
            subject,
            value,
            metadata,
            created_at
        FROM temporal_events
        WHERE event_type = ?
          AND subject = ?
        ORDER BY id DESC
        LIMIT 1
    """, (
        event_type,
        subject,
    ))

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row["id"],
        "event_type": row["event_type"],
        "subject": row["subject"],
        "value": row["value"],
        "metadata": row["metadata"],
        "created_at": row["created_at"],
    }