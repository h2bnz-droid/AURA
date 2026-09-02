from core.cognitive_behavior import CognitiveBehavior


class CognitiveState:

    def __init__(
        self,
        mindset=None,
        emotion=None,
        source="test",
    ):
        self.mindset = mindset
        self.emotion = emotion
        self.source = source


def test_resilient_behavior():

    behavior = CognitiveBehavior()

    state = CognitiveState(
        mindset="resilient",
    )

    result = behavior.build(state)

    assert result is not None
    assert "kesulitan" in result


def test_anxious_behavior():

    behavior = CognitiveBehavior()

    state = CognitiveState(
        emotion="anxious",
    )

    result = behavior.build(state)

    assert result is not None
    assert "menenangkan" in result


def test_combined_cognitive_behavior():

    behavior = CognitiveBehavior()

    state = CognitiveState(
        mindset="resilient",
        emotion="anxious",
    )

    result = behavior.build(state)

    assert "menenangkan" in result
    assert "kesulitan" in result


def test_empty_cognitive_state_returns_none():

    behavior = CognitiveBehavior()

    state = CognitiveState()

    result = behavior.build(state)

    assert result is None