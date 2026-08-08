from enum import Enum, auto


class DecisionIntent(Enum):
    COMPARE = auto()
    DECIDE = auto()
    UNKNOWN = auto()