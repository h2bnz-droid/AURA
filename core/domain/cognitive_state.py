from dataclasses import dataclass
from typing import Optional


@dataclass
class CognitiveState:
    mindset: Optional[str] = None
    emotion: Optional[str] = None
    source: str = "system"