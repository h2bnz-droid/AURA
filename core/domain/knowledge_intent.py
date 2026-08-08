from enum import Enum, auto


class KnowledgeIntent(Enum):
    SEARCH = auto()
    EXPLAIN = auto()
    UNKNOWN = auto()