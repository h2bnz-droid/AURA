from datetime import datetime

from database.goals import (
    create_goal,
    get_active_goals,
    update_progress,
    complete_goal,
    abandon_goal
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

def increase_progress(goal_id, amount: int):
    current_goals = get_active_goals()
    for goal in current_goals:
        if goal[0] == goal_id:
            new_progress = min(goal[6] + amount, 100)  # Assuming progress is at index 6
            update_progress(goal_id, new_progress)
            break

def finish_goal(goal_id: int):
    complete_goal(goal_id)

def abandon(goal_id: int):
    abandon_goal(goal_id)

def find_active_goal(title: str):
    """Find a single active goal using a case-insensitive title match."""
    query = title.strip().casefold()
    if not query:
        return None

    partial_matches = []
    for goal in get_active_goals():
        normalized_title = goal["title"].casefold()
        if normalized_title == query:
            return goal
        if query in normalized_title or normalized_title in query:
            partial_matches.append(goal)
    return partial_matches[0] if len(partial_matches) == 1 else None
