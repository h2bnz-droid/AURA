from unittest.mock import patch

from core.engines.engine_manager import EngineManager
from core.engines.reflection_engine import ReflectionEngine


def test_engine_manager_contains_reflection_engine():
    manager = EngineManager()

    assert any(
        isinstance(engine, ReflectionEngine)
        for engine in manager.engines
    )


@patch("core.engines.reflection_engine.get_profile")
@patch("core.engines.reflection_engine.recall_all")
@patch("core.engines.reflection_engine.active_goals")
def test_engine_manager_handles_reflection(
    mock_goals,
    mock_memory,
    mock_profile,
):
    mock_profile.return_value = {
        "name": "Budi"
    }
    mock_memory.return_value = []
    mock_goals.return_value = []

    manager = EngineManager()

    result = manager.process(
        "Aku ingin merenung"
    )

    assert result is not None
    assert "merenung" in result.lower()
