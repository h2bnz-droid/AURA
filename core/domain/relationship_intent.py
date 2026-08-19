from enum import Enum, auto


class RelationshipIntent(Enum):
    CREATE = auto()
    SHOW = auto()
    UPDATE = auto()
    UNKNOWN_INTENT = auto()