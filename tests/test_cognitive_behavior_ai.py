from unittest.mock import patch

from core.chat import ask


@patch("core.chat.chat")
@patch("core.chat.add")
@patch("core.chat.build_context")
def test_cognitive_behavior_is_sent_to_ai(
    mock_build_context,
    mock_add,
    mock_chat,
):
    context = type(
        "Context",
        (),
        {
            "profile": None,
            "memories": [],
            "history": [],
            "emotion": None,
            "temporal": [],
            "reflections": [],
            "relationships": [],
            "cognitive_model": (),
            "mindsets": [],
            "active_mindset": None,
            "personalization": None,
            "long_term_context": [],
            "cognitive_state": None,
            "integrated_cognitive_context": None,
            "cognitive_behavior": (
                "Gunakan nada yang menenangkan."
            ),
            "user_input": "Aku merasa khawatir.",
        },
    )()

    mock_build_context.return_value = context
    mock_chat.return_value = "Jawaban AURA"

    result = ask("Aku merasa khawatir.")

    assert result == "Jawaban AURA"

    messages = mock_chat.call_args[0][0]

    user_prompt = messages[1]["content"]

    assert "[COGNITIVE BEHAVIOR]" in user_prompt

    assert (
        "Gunakan nada yang menenangkan."
        in user_prompt
    )