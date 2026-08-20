from dataclasses import dataclass
from datetime import datetime


@dataclass
class CognitiveAttribute:
    attribute_name: str
    attribute_value: str
    category: str
    source: str
    confidence: float
    created_at: str
    updated_at: str


@dataclass
class PersonalCognitiveModel:
    attributes: list[CognitiveAttribute]