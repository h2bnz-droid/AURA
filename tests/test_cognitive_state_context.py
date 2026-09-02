from unittest.mock import patch

from core.context_builder import build_context
from core.domain.cognitive_state import CognitiveState


@patch(
    "core.context_builder.cognitive_state_service"
)
def test_build_context_contains_cognitive_state(
    mock_cognitive_state_service,
):
    state = CognitiveState(
        mindset="resilient",
        emotion="frustrated",
        source="user_message",
    )

    mock_cognitive_state_service.latest.return_value = state

    context = build_context(
        "Aku gagal lagi belajar Python"
    )

    assert hasattr(context, "cognitive_state")

    assert context.cognitive_state is state

    mock_cognitive_state_service.latest.assert_called_once()