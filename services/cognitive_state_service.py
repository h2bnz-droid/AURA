from core.domain.cognitive_state import CognitiveState
from core.domain.cognitive_state_history import (
    CognitiveStateHistory,
    CognitiveStateHistoryItem,
)
from database.cognitive_states import (
    create_table,
    get_latest_state,
    get_state_history,
    save_state,
)


class CognitiveStateService:

    def initialize(self):
        create_table()

    def record_mindset(
        self,
        mindset: str,
        confidence: float = 0.0,
        source: str = "system",
    ) -> CognitiveState:

        save_state(
            state_type="mindset",
            value=mindset,
            confidence=confidence,
            source=source,
        )

        return CognitiveState(
            mindset=mindset,
            source=source,
        )

    def record_emotion(
        self,
        emotion: str,
        confidence: float = 0.0,
        source: str = "system",
    ) -> CognitiveState:

        save_state(
            state_type="emotion",
            value=emotion,
            confidence=confidence,
            source=source,
        )

        return CognitiveState(
            emotion=emotion,
            source=source,
        )

    def latest(self) -> CognitiveState:
        mindset_state = get_latest_state("mindset")
        emotion_state = get_latest_state("emotion")

        if mindset_state is None and emotion_state is None:
            return CognitiveState()

        source = self._resolve_source(
            mindset_state,
            emotion_state,
        )

        return CognitiveState(
            mindset=(
                mindset_state["value"]
                if mindset_state is not None
                else None
            ),
            emotion=(
                emotion_state["value"]
                if emotion_state is not None
                else None
            ),
            source=source,
        )

    def history(
        self,
        state_type: str | None = None,
        limit: int = 10,
    ) -> list[dict]:

        return get_state_history(
            state_type=state_type,
            limit=limit,
        )

    def history_context(
        self,
        state_type: str | None = None,
        limit: int = 10,
    ) -> CognitiveStateHistory:

        records = self.history(
            state_type=state_type,
            limit=limit,
        )

        items = [
            CognitiveStateHistoryItem(
                state_type=record["state_type"],
                value=record["value"],
                confidence=record["confidence"],
                source=record["source"],
                created_at=record.get("created_at"),
            )
            for record in records
        ]

        return CognitiveStateHistory(items=items)

    def _resolve_source(
        self,
        mindset_state,
        emotion_state,
    ) -> str:

        if mindset_state is not None:
            return mindset_state["source"]

        if emotion_state is not None:
            return emotion_state["source"]

        return "system"