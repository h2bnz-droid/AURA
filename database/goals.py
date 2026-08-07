from database.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        category TEXT,
        status TEXT,
        priority INTEGER,
        progress INTEGER,
        created_at TEXT,
        updated_at TEXT,
        target_date TEXT           
    )
    """)

    conn.commit()
    conn.close() 

def create_goal(title, description, category, status,priority, progress, created_at, updated_at, target_date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO goals (title, description, category, status, priority, progress, created_at, updated_at, target_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, description, category, status, priority, progress, created_at, updated_at, target_date))

    conn.commit()
    conn.close()

def get_active_goals():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM goals
        WHERE status = 'active'
        ORDER BY priority DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows           
    

def update_progress(goal_id, progress):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
           UPDATE goals
           SET progress = ?, updated_at = CURRENT_TIMESTAMP
           WHERE id = ?
    """, (progress, goal_id))
    conn.commit()
    conn.close()

def complete_goal(goal_id):
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("""
        UPDATE goals
        SET status = 'completed',
        progress = 100,
        updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (goal_id,))
   conn.commit()
   conn.close()

def abandon_goal(goal_id):
   conn = get_connection()
   cursor = conn.cursor()
   cursor.execute("""
        UPDATE goals
        SET status = 'abandoned', updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
   """, (goal_id,))
   conn.commit()
   conn.close()

def find_goal_by_title(title):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM goals
        WHERE title = ?
    """, (title,))

    row = cursor.fetchone()

    conn.close()

    return row

def get_goal(goal_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM goals
        WHERE id = ?
    """, (goal_id,))

    row = cursor.fetchone()

    conn.close()

    return row
