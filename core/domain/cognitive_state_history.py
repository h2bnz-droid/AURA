from dataclasses import dataclass, field
from typing import Any


@dataclass
class CognitiveStateHistoryItem:
    state_type: str
    value: Any
    confidence: float
    source: str
    created_at: str | None = None


@dataclass
class CognitiveStateHistory:
    items: list[CognitiveStateHistoryItem] = field(
        default_factory=list
    )

    def latest(self) -> CognitiveStateHistoryItem | None:
        if not self.items:
            return None

        return self.items[0]

    def filter_by_type(
        self,
        state_type: str,
    ) -> list[CognitiveStateHistoryItem]:

        return [
            item
            for item in self.items
            if item.state_type == state_type
        ]