from database.connection import get_connection


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        memory_key TEXT,
        memory_value TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

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

def search_memories(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, memory_key, memory_value
        FROM memories
        WHERE memory_value LIKE ?
           OR memory_key LIKE ?
        ORDER BY id DESC
        LIMIT 10
    """, (f"%{keyword}%", f"%{keyword}%"))

    rows = cursor.fetchall()

    conn.close()

    return rows