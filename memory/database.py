import sqlite3
from pathlib import Path

DB_PATH = Path("memory") / "aura.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    return conn


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profile (
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