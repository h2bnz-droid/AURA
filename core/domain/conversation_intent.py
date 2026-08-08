from enum import Enum, auto


class ConversationIntent(Enum):
    GREETING = auto()
    CHAT = auto()
    UNKNOWN = auto()