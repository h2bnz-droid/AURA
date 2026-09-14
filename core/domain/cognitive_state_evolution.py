from dataclasses import dataclass
from typing import Any


@dataclass
class CognitiveStateEvolution:
    state_type: str
    previous_value: Any = None
    current_value: Any = None
    status: str = "unknown"

    @property
    def has_previous_state(self) -> bool:
        return self.previous_value is not None

    @property
    def has_current_state(self) -> bool:
        return self.current_value is not None