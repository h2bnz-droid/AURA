from dataclasses import dataclass, field
from typing import Any


@dataclass
class CognitiveContextItem:
    category: str
    value: Any
    source: str
    confidence: float
    relevance: float = 0.0


@dataclass
class IntegratedCognitiveContext:
    stable: list[CognitiveContextItem] = field(default_factory=list)
    relevant: list[CognitiveContextItem] = field(default_factory=list)
    recent: list[CognitiveContextItem] = field(default_factory=list)

    def all_items(self) -> list[CognitiveContextItem]:
        return (
            self.stable
            + self.relevant
            + self.recent
        )

@dataclass
class CognitiveContextItem:
    category: str
    value: Any
    source: str
    confidence: float
    relevance: float = 0.0