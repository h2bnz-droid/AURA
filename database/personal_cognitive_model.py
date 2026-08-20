from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personal_cognitive_model (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        attribute_name TEXT NOT NULL,
        attribute_value TEXT NOT NULL,
        category TEXT NOT NULL,
        source TEXT NOT NULL,
        confidence REAL NOT NULL,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_attribute(
    attribute_name: str,
    attribute_value: str,
    category: str,
    source: str,
    confidence: float,
    created_at: str,
    updated_at: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO personal_cognitive_model (
            attribute_name,
            attribute_value,
            category,
            source,
            confidence,
            created_at,
            updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        attribute_name,
        attribute_value,
        category,
        source,
        confidence,
        created_at,
        updated_at,
    ))

    conn.commit()
    conn.close()


def get_attribute(attribute_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM personal_cognitive_model
        WHERE attribute_name = ?
        ORDER BY updated_at DESC
        LIMIT 1
    """, (attribute_name,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_all_attributes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM personal_cognitive_model
        ORDER BY updated_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_attribute(
    attribute_name: str,
    attribute_value: str,
    category: str,
    source: str,
    confidence: float,
    updated_at: str,
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE personal_cognitive_model
        SET attribute_value = ?,
            category = ?,
            source = ?,
            confidence = ?,
            updated_at = ?
        WHERE attribute_name = ?
    """, (
        attribute_value,
        category,
        source,
        confidence,
        updated_at,
        attribute_name,
    ))

    conn.commit()
    conn.close()


def delete_attribute(attribute_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM personal_cognitive_model
        WHERE attribute_name = ?
    """, (attribute_name,))

    conn.commit()
    conn.close()