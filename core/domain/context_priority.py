from dataclasses import dataclass


@dataclass
class ContextPriority:
    category: str
    value: str
    priority: float
    source: str | None = None
    confidence: float | None = None
    relevance: float | None = None