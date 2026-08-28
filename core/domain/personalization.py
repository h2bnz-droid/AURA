from dataclasses import dataclass


@dataclass
class PersonalizationPreference:
    name: str
    value: str
    source: str
    confidence: float
    created_at: str
    updated_at: str


@dataclass
class PersonalizationSignal:
    name: str
    value: str
    source: str
    confidence: float
    timestamp: str