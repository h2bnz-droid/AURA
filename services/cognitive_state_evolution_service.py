from core.domain.cognitive_state import CognitiveState
from core.domain.cognitive_state_evolution import (
    CognitiveStateEvolution,
)
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
)


class CognitiveStateEvolutionService:

    def analyze(
        self,
        cognitive_state: CognitiveState | None,
        cognitive_state_history: CognitiveStateHistory | None,
    ) -> list[CognitiveStateEvolution]:

        if cognitive_state is None:
            cognitive_state = CognitiveState()

        if cognitive_state_history is None:
            cognitive_state_history = CognitiveStateHistory()

        evolutions = []

        mindset_evolution = self._analyze_state(
            state_type="mindset",
            current_value=cognitive_state.mindset,
            history=cognitive_state_history,
        )

        emotion_evolution = self._analyze_state(
            state_type="emotion",
            current_value=cognitive_state.emotion,
            history=cognitive_state_history,
        )

        evolutions.append(mindset_evolution)
        evolutions.append(emotion_evolution)

        return evolutions

    def _analyze_state(
        self,
        state_type: str,
        current_value,
        history: CognitiveStateHistory,
    ) -> CognitiveStateEvolution:

        history_items = history.filter_by_type(
            state_type
        )

        previous_value = None

        if history_items:
            previous_value = history_items[0].value

        status = self._resolve_status(
            previous_value=previous_value,
            current_value=current_value,
        )

        return CognitiveStateEvolution(
            state_type=state_type,
            previous_value=previous_value,
            current_value=current_value,
            status=status,
        )

    def _resolve_status(
        self,
        previous_value,
        current_value,
    ) -> str:

        if previous_value is None:
            return "unknown"

        if current_value is None:
            return "unknown"

        if previous_value == current_value:
            return "stable"

        return "transition"