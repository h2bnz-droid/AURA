from unittest.mock import patch

from core.chat import ask


@patch("core.chat.chat")
@patch("core.chat.add")
@patch("core.chat.build_context")
def test_active_mindset_is_sent_to_ai(
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
            "active_mindset": type(
                "Mindset",
                (),
                {
                    "name": "resilient",
                    "description": "Kesulitan dapat dihadapi.",
                },
            )(),
            "personalization": None,
            "long_term_context": [],
            "integrated_cognitive_context": None,
            "user_input": "Aku gagal lagi.",
        },
    )()

    mock_build_context.return_value = context
    mock_chat.return_value = "Jawaban AURA"

    result = ask("Aku gagal lagi.")

    assert result == "Jawaban AURA"

    messages = mock_chat.call_args.args[0]

    user_prompt = messages[1]["content"]

    assert "[ACTIVE MINDSET]" in user_prompt
    assert "resilient" in user_prompt
    assert "Kesulitan dapat dihadapi." in user_prompt