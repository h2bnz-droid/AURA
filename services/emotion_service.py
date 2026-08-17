from database.emotions import (
    get_emotion_history,
    get_latest_emotion,
    save_emotion,
)


def record_emotion(
    emotion: str,
    intensity: float = 0.0,
    source: str = "user_message",
):
    save_emotion(
        emotion,
        intensity,
        source,
    )


def latest_emotion():
    return get_latest_emotion()


def emotion_history(limit: int = 10):
    return get_emotion_history(limit)


def find_emotion(emotion: str):
    query = emotion.strip().casefold()

    if not query:
        return None

    for item in get_emotion_history():
        if item["emotion"].casefold() == query:
            return item

    return None