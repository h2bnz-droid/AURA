from core.domain.cognitive_state import CognitiveState


def test_cognitive_state_defaults():
    state = CognitiveState()

    assert state.mindset is None
    assert state.emotion is None
    assert state.source == "system"


def test_cognitive_state_with_values():
    state = CognitiveState(
        mindset="growth",
        emotion="motivated",
        source="mindset_engine",
    )

    assert state.mindset == "growth"
    assert state.emotion == "motivated"
    assert state.source == "mindset_engine"