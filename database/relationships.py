from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relationships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        person_name TEXT NOT NULL,
        relationship_type TEXT NOT NULL,
        status TEXT,
        note TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_relationship(
    person_name: str,
    relationship_type: str,
    status: str | None,
    note: str | None,
    created_at: str,
    updated_at: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO relationships (
            person_name,
            relationship_type,
            status,
            note,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        person_name,
        relationship_type,
        status,
        note,
        created_at,
        updated_at,
    ))

    conn.commit()
    conn.close()


def get_relationship(person_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM relationships
        WHERE person_name = ?
        ORDER BY updated_at DESC
        LIMIT 1
    """, (person_name,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_all_relationships():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM relationships
        ORDER BY updated_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_relationship(
    person_name: str,
    relationship_type: str,
    status: str | None,
    note: str | None,
    updated_at: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE relationships
        SET relationship_type = ?,
            status = ?,
            note = ?,
            updated_at = ?
        WHERE person_name = ?
    """, (
        relationship_type,
        status,
        note,
        updated_at,
        person_name,
    ))

    conn.commit()
    conn.close()