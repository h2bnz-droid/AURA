from unittest.mock import patch

from core.context_builder import build_context


@patch("core.context_builder.latest")
@patch("core.context_builder.latest_emotion")
@patch("core.context_builder.event_history")
@patch("core.context_builder.history")
@patch("core.context_builder.owner_name")
def test_context_builder_includes_reflections(
    mock_owner,
    mock_history,
    mock_temporal,
    mock_emotion,
    mock_reflections,
):
    mock_owner.return_value = "Budi"
    mock_history.return_value = []
    mock_temporal.return_value = []
    mock_emotion.return_value = None
    mock_reflections.return_value = [
        {
            "summary": "Aku belajar bahwa konsistensi lebih penting.",
            "insights": "Konsistensi",
            "questions": "Apa yang bisa diperbaiki?",
        }
    ]

    context = build_context("Apa yang kupelajari?")

    assert len(context.reflections) == 1
    assert (
        context.reflections[0]["summary"]
        == "Aku belajar bahwa konsistensi lebih penting."
    )
