from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile(
        id INTEGER PRIMARY KEY,
        name TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def get_profile():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM profile LIMIT 1")
    row = cursor.fetchone()

    conn.close()

    return row


def save_profile(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM profile")

    cursor.execute(
        "INSERT INTO profile(name) VALUES(?)",
        (name,)
    )

    conn.commit()
    conn.close()

def update_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE profile SET name=? WHERE id=1",
        (name,)
    )

    conn.commit()
    conn.close()
