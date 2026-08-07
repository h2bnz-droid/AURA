from datetime import datetime

from database.reflections import (
    create_reflection,
    get_latest_reflections,
    get_all_reflections,
)


def save(
    summary: str,
    insights: str,
    questions: str,
) -> None:

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    create_reflection(
        summary,
        insights,
        questions,
        created_at,
    )


def latest(limit: int = 5):
    return get_latest_reflections(limit)


def all():
    return get_all_reflections()