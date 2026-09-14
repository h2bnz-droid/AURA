from core.domain.cognitive_state import CognitiveState
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)
from services.cognitive_state_evolution_service import (
    CognitiveStateEvolutionService,
)


def test_mindset_stable():

    service = CognitiveStateEvolutionService()

    cognitive_state = CognitiveState(
        mindset="growth",
    )

    history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="growth",
                confidence=0.9,
                source="user_input",
            )
        ]
    )

    evolutions = service.analyze(
        cognitive_state,
        history,
    )

    mindset = evolutions[0]

    assert mindset.status == "stable"


def test_mindset_transition():

    service = CognitiveStateEvolutionService()

    cognitive_state = CognitiveState(
        mindset="resilient",
    )

    history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="growth",
                confidence=0.9,
                source="user_input",
            )
        ]
    )

    evolutions = service.analyze(
        cognitive_state,
        history,
    )

    mindset = evolutions[0]

    assert mindset.previous_value == "growth"
    assert mindset.current_value == "resilient"
    assert mindset.status == "transition"


def test_emotion_transition():

    service = CognitiveStateEvolutionService()

    cognitive_state = CognitiveState(
        emotion="focused",
    )

    history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="emotion",
                value="frustrated",
                confidence=0.8,
                source="user_input",
            )
        ]
    )

    evolutions = service.analyze(
        cognitive_state,
        history,
    )

    emotion = evolutions[1]

    assert emotion.status == "transition"


def test_unknown_without_history():

    service = CognitiveStateEvolutionService()

    cognitive_state = CognitiveState(
        mindset="growth",
    )

    history = CognitiveStateHistory()

    evolutions = service.analyze(
        cognitive_state,
        history,
    )

    mindset = evolutions[0]

    assert mindset.status == "unknown"


def test_unknown_without_current_state():

    service = CognitiveStateEvolutionService()

    cognitive_state = CognitiveState()

    history = CognitiveStateHistory(
        items=[
            CognitiveStateHistoryItem(
                state_type="mindset",
                value="growth",
                confidence=0.9,
                source="user_input",
            )
        ]
    )

    evolutions = service.analyze(
        cognitive_state,
        history,
    )

    mindset = evolutions[0]

    assert mindset.status == "unknown"