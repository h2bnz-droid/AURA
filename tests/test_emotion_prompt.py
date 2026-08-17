from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_contains_emotion():
    context = AuraContext(
        "Aku sedang senang hari ini"
    )

    context.emotion = {
        "emotion": "happy",
        "intensity": 0.8,
        "source": "user_message",
    }

    prompt = PromptBuilder().build(context)

    assert "[EMOTION]" in prompt
    assert "Emosi terakhir: happy" in prompt
    assert "Intensitas: 0.8" in prompt


def test_prompt_without_emotion_does_not_add_emotion_section():
    context = AuraContext("Halo AURA")

    prompt = PromptBuilder().build(context)

    assert "[EMOTION]" not in prompt