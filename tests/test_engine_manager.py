from core.engines.engine_manager import EngineManager


def test_planner_engine_integration():
    manager = EngineManager()

    result = manager.process("buat rencana untuk belajar Python")

    assert result is not None


def test_decision_engine_integration():
    manager = EngineManager()

    result = manager.process("bandingkan laptop A dan laptop B")

    assert result is not None


def test_knowledge_engine_integration():
    manager = EngineManager()

    result = manager.process("cari informasi tentang Python")

    assert result is not None


def test_conversation_engine_fallback():
    manager = EngineManager()

    result = manager.process("hari ini aku merasa produktif")

    assert result is not None


def test_unknown_message():
    manager = EngineManager()

    result = manager.process("")

    assert result is None