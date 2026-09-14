from core.context import AuraContext


def test_aura_context_has_cognitive_state_evolution():

    context = AuraContext(
        user_input="Saya sedang fokus belajar",
    )

    assert hasattr(
        context,
        "cognitive_state_evolution",
    )


def test_cognitive_state_evolution_default_is_none():

    context = AuraContext(
        user_input="Saya sedang fokus belajar",
    )

    assert context.cognitive_state_evolution is None