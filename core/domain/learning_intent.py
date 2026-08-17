from enum import Enum


class LearningIntent(Enum):
    START = "start"
    PROGRESS = "progress"
    SHOW = "show"
    UNKNOWN = "unknown"