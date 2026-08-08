from enum import Enum, auto

class PlannerIntent(Enum):
    """Intent yang dikenali oleh PlannerEngine."""

    CREATE_PLAN = auto()
    SHOW_PLAN = auto()
    UNKNOWN = auto()