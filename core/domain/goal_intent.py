from enum import Enum, auto


class GoalIntent(Enum):
    """Intent yang berkaitan dengan Goal pengguna."""

    CREATE = auto()
    UPDATE = auto()
    COMPLETE = auto()
    ABANDON = auto()
    SHOW = auto()
    UNKNOWN = auto()