from enum import Enum


class ProfileIntent(Enum):
    CREATE = "create"
    UPDATE = "update"
    SHOW = "show"
    UNKNOWN = "unknown"