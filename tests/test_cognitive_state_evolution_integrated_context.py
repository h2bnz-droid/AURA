from types import SimpleNamespace

from core.context_builder import (
    _add_cognitive_state_evolution_to_context,
)
from core.domain.cognitive_state_evolution import (
    CognitiveStateEvolution,
)


def test_evolution_added_to_integrated_context():

    context = SimpleNamespace(recent=[])

    evolution = [
        CognitiveStateEvolution(
            state_type="mindset",
            previous_value="growth",
            current_value="resilient",
            status="transition",
        )
    ]

    _add_cognitive_state_evolution_to_context(
        context,
        evolution,
    )

    assert len(context.recent) == 1
    assert context.recent[0].category == "mindset_evolution"
    assert context.recent[0].value == "transition"


def test_emotion_evolution_category():

    context = SimpleNamespace(recent=[])

    evolution = [
        CognitiveStateEvolution(
            state_type="emotion",
            previous_value="frustrated",
            current_value="focused",
            status="transition",
        )
    ]

    _add_cognitive_state_evolution_to_context(
        context,
        evolution,
    )

    assert context.recent[0].category == "emotion_evolution"


def test_unknown_evolution_is_not_added():

    context = SimpleNamespace(recent=[])

    evolution = [
        CognitiveStateEvolution(
            state_type="mindset",
            status="unknown",
        )
    ]

    _add_cognitive_state_evolution_to_context(
        context,
        evolution,
    )

    assert len(context.recent) == 0


def test_empty_evolution_is_handled():

    context = SimpleNamespace(recent=[])

    _add_cognitive_state_evolution_to_context(
        context,
        [],
    )

    assert len(context.recent) == 0