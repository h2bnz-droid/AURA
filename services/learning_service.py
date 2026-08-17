from database.learning import (
    create_learning,
    get_active_learning,
    update_progress,
)


def start_learning(topic: str):
    create_learning(topic)


def active_learning():
    return get_active_learning()


def update_learning_progress(topic: str, progress: int):
    update_progress(topic, progress)


def find_learning(topic: str):
    query = topic.strip().casefold()

    if not query:
        return None

    for learning in get_active_learning():
        if learning["topic"].casefold() == query:
            return learning

    return None