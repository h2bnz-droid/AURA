from database.temporal import (
    save_event,
    get_history,
    get_latest,
)


def record_event(
    event_type: str,
    subject: str,
    value: str | None = None,
    metadata: str | None = None,
):
    save_event(
        event_type,
        subject,
        value,
        metadata,
    )


def event_history(
    event_type: str | None = None,
    subject: str | None = None,
):
    return get_history(
        event_type=event_type,
        subject=subject,
    )


def latest_event(
    event_type: str,
    subject: str,
):
    return get_latest(
        event_type,
        subject,
    )


def calculate_trend(values: list[float]):
    if len(values) < 2:
        return "stable"

    if values[-1] > values[0]:
        return "increasing"

    if values[-1] < values[0]:
        return "decreasing"

    return "stable"