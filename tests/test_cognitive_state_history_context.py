from core.context import AuraContext


def test_aura_context_has_cognitive_state_history():
    context = AuraContext("Halo")

    assert hasattr(
        context,
        "cognitive_state_history",
    )


def test_cognitive_state_history_defaults_to_none():
    context = AuraContext("Halo")

    assert context.cognitive_state_history is None