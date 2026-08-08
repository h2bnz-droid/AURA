import json
from datetime import datetime

from database.plans import (
    create_plan, 
    get_plans
)

DEFAULT_STATUS = "active"

def save_plan(goal: str, steps: list[str]) -> None:
    """
    Menyimpan rencana ke database.
    """
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = created_at

    steps_json = json.dumps(steps, ensure_ascii=False)

    create_plan(
        goal,
        steps_json,
        DEFAULT_STATUS,
        created_at,
        updated_at
    )

def all_plans() -> list:
    """
    Mengambil semua rencana dari database.
    """
    return get_plans()
