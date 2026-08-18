from database.temporal import (
    create_table,
    save_event,
    get_history,
    get_latest,
)


def test_temporal_database_saves_and_reads_events():
    create_table()

    save_event(
        "learning",
        "Python",
        "50",
    )

    history = get_history(
        event_type="learning",
        subject="Python",
    )

    assert len(history) >= 1
    assert history[-1]["event_type"] == "learning"
    assert history[-1]["subject"] == "Python"
    assert history[-1]["value"] == "50"


def test_temporal_database_gets_latest_event():
    create_table()

    save_event(
        "emotion",
        "current",
        "happy",
    )

    latest = get_latest(
        "emotion",
        "current",
    )

    assert latest is not None
    assert latest["event_type"] == "emotion"
    assert latest["value"] == "happy"