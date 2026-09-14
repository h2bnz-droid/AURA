from core.context_builder import build_context


def test_context_builder_has_cognitive_state_evolution():

    context = build_context(
        "Saya sedang belajar dengan fokus"
    )

    assert hasattr(
        context,
        "cognitive_state_evolution",
    )


def test_context_builder_builds_cognitive_state_evolution():

    context = build_context(
        "Saya sedang belajar dengan fokus"
    )

    assert context.cognitive_state_evolution is not None


def test_context_builder_cognitive_state_evolution_has_states():

    context = build_context(
        "Saya sedang belajar dengan fokus"
    )

    evolution = context.cognitive_state_evolution

    assert len(evolution) == 2


def test_context_builder_cognitive_state_evolution_types():

    context = build_context(
        "Saya sedang belajar dengan fokus"
    )

    evolution = context.cognitive_state_evolution

    assert evolution[0].state_type == "mindset"
    assert evolution[1].state_type == "emotion"