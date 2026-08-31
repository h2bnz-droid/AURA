from core.engines.engine_manager import EngineManager
from core.engines.mindset_engine import MindsetEngine


def test_engine_manager_contains_mindset_engine():
    manager = EngineManager()

    assert any(
        isinstance(engine, MindsetEngine)
        for engine in manager.engines
    )
