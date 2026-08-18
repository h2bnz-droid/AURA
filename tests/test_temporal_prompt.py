from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_includes_temporal_context():
    context = AuraContext(
        "Bagaimana perkembangan Python?"
    )

    context.temporal = [
        {
            "event_type": "learning",
            "subject": "Python",
            "value": "50",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "[TEMPORAL CONTEXT]" in prompt
    assert "learning" in prompt
    assert "Python" in prompt
    assert "50" in prompt


def test_prompt_builder_handles_empty_temporal_context():
    context = AuraContext(
        "Halo AURA"
    )

    context.temporal = []

    prompt = PromptBuilder().build(context)

    assert "[TEMPORAL CONTEXT]" not in prompt
    assert "CURRENT USER MESSAGE" in prompt