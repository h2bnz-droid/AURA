from dataclasses import dataclass
from datetime import datetime


@dataclass
class Goal:
    id: int | None
    title: str
    description: str = ""
    category: str = "general"
    status: str = "active"
    priority: int = 3
    progress: int = 0
    created_at: datetime | None = None
    updated_at: datetime | None = None
    target_date: datetime | None = None