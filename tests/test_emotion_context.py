from unittest.mock import patch

from core.context_builder import build_context


@patch("core.context_builder.latest_emotion")
def test_context_contains_current_emotion(mock_latest):
    mock_latest.return_value = {
        "emotion": "happy",
        "intensity": 0.8,
        "source": "user_message",
    }

    context = build_context("Aku senang hari ini")

    assert context.emotion is not None
    assert context.emotion["emotion"] == "happy"
    assert context.emotion["intensity"] == 0.8


@patch("core.context_builder.latest_emotion")
def test_context_handles_empty_emotion(mock_latest):
    mock_latest.return_value = None

    context = build_context("Halo AURA")

    assert context.emotion is None