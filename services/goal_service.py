from datetime import datetime

from database.goals import (
    create_goal,
    get_active_goals,
    update_progress,
    complete_goal
)

DEFAULT_DESCRIPTION = "Deskripsi goal belum ditentukan."
DEFAULT_CATEGORY = "General"
DEFAULT_PRIORITY = 1

def add_goal(
    title: str,
    description: str = DEFAULT_DESCRIPTION,
    category: str = DEFAULT_CATEGORY,
    priority: int = DEFAULT_PRIORITY,
    target_date: str | None = None,
):
    status = "active"
    progress = 0
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at

    create_goal(
        title,
        description,
        category,
        status,
        priority,
        progress,
        created_at,
        updated_at,
        target_date
    )

def active_goals():
    return get_active_goals()

def set_progress(goal_id: int, progress: int):
    update_progress(goal_id, progress)

def finish_goal(goal_id: int):
    complete_goal(goal_id)