from unittest.mock import patch

from core.context_builder import build_context
from core.prompt_builder import PromptBuilder


@patch("core.context_builder.latest_emotion")
def test_emotion_flows_from_context_to_prompt(mock_latest):
    mock_latest.return_value = {
        "emotion": "anxious",
        "intensity": 0.7,
        "source": "user_message",
    }

    context = build_context(
        "Aku khawatir menghadapi ujian"
    )

    prompt = PromptBuilder().build(context)

    assert context.emotion["emotion"] == "anxious"
    assert "Emosi terakhir: anxious" in prompt
    assert "Intensitas: 0.7" in prompt