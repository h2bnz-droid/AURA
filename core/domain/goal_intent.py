from enum import Enum


class GoalIntent(Enum):
    """Intent yang berkaitan dengan Goal pengguna."""

    CREATE = "create"
    UPDATE = "update"
    COMPLETE = "complete"
    ABANDON = "abandon"
    SHOW = "show"
    UNKNOWN = "unknown"