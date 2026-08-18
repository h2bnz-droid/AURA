from unittest.mock import patch

from core.context_builder import build_context


@patch("core.context_builder.event_history")
def test_context_builder_includes_temporal_events(
    mock_history,
):
    mock_history.return_value = [
        {
            "id": 1,
            "event_type": "learning",
            "subject": "Python",
            "value": "50",
            "metadata": None,
            "created_at": "2026-01-01 10:00:00",
        }
    ]

    context = build_context(
        "Bagaimana perkembangan Python?"
    )

    assert len(context.temporal) == 1
    assert context.temporal[0]["subject"] == "Python"
    assert context.temporal[0]["value"] == "50"