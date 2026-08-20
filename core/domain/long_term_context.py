from dataclasses import dataclass


@dataclass
class LongTermContext:
    content: str
    category: str
    source: str
    confidence: float
    relevance: float
    created_at: str
    updated_at: str