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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        memory_key TEXT NOT NULL,
        memory_value TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        role TEXT NOT NULL,
        message TEXT NOT NULL,
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

def save_memory(category, key, value):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memories(category, memory_key, memory_value)
        VALUES (?, ?, ?)
    """, (category, key, value))

    conn.commit()
    conn.close()

def get_memory(key):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT memory_value
        FROM memories
        WHERE memory_key = ?
        ORDER BY id DESC
        LIMIT 1
    """, (key,))

    row = cursor.fetchone()

    conn.close()

    return row            

def get_all_memories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, memory_key, memory_value
        FROM memories
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def save_conversation(role, message):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversations(role, message)
        VALUES (?, ?)
    """, (role, message))

    conn.commit()
    conn.close()

def get_recent_conversations(limit=10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, message
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    conn.close()

    return list(reversed(rows))    