from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_includes_long_term_context():
    context = AuraContext(
        "Apa tujuan karierku?"
    )

    context.long_term_context = [
        {
            "content": "Software Engineer",
            "category": "aspiration",
            "source": "personal_cognitive_model",
        },
        {
            "content": "Python",
            "category": "skill",
            "source": "memory",
        },
    ]

    prompt = PromptBuilder().build(context)

    assert "[LONG-TERM CONTEXT]" in prompt
    assert "Software Engineer" in prompt
    assert "Python" in prompt


def test_prompt_excludes_empty_long_term_context():
    context = AuraContext("Halo")

    context.long_term_context = []

    prompt = PromptBuilder().build(context)

    assert "[LONG-TERM CONTEXT]" not in prompt