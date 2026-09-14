from core.domain.cognitive_state_evolution import (
    CognitiveStateEvolution,
)


def test_cognitive_state_evolution_creation():

    evolution = CognitiveStateEvolution(
        state_type="mindset",
        previous_value="growth",
        current_value="resilient",
        status="transition",
    )

    assert evolution.state_type == "mindset"
    assert evolution.previous_value == "growth"
    assert evolution.current_value == "resilient"
    assert evolution.status == "transition"


def test_cognitive_state_evolution_has_previous_state():

    evolution = CognitiveStateEvolution(
        state_type="emotion",
        previous_value="frustrated",
    )

    assert evolution.has_previous_state is True


def test_cognitive_state_evolution_without_previous_state():

    evolution = CognitiveStateEvolution(
        state_type="emotion",
    )

    assert evolution.has_previous_state is False


def test_cognitive_state_evolution_has_current_state():

    evolution = CognitiveStateEvolution(
        state_type="mindset",
        current_value="focused",
    )

    assert evolution.has_current_state is True


def test_cognitive_state_evolution_without_current_state():

    evolution = CognitiveStateEvolution(
        state_type="mindset",
    )

    assert evolution.has_current_state is False


def test_cognitive_state_evolution_default_status():

    evolution = CognitiveStateEvolution(
        state_type="emotion",
    )

    assert evolution.status == "unknown"