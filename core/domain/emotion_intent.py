from enum import Enum


class EmotionIntent(Enum):
    DETECT = "detect"
    SHOW = "show"
    TRACK = "track"
    UNKNOWN = "unknown"