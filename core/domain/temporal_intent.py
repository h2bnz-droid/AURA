from enum import Enum


class TemporalIntent(Enum):
    TREND = "trend"
    HISTORY = "history"
    STATE = "state"
    UNKNOWN = "unknown"