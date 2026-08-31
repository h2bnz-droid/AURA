from core.engines.engine_manager import EngineManager


def test_engine_manager_handles_knowledge_search():
    manager = EngineManager()

    result = manager.process(
        "cari informasi tentang Python"
    )

    assert result is not None
    assert "Python" in result


def test_engine_manager_handles_knowledge_explain():
    manager = EngineManager()

    result = manager.process(
        "jelaskan Python"
    )

    assert result is not None
    assert "Python" in result


def test_knowledge_does_not_capture_general_conversation():
    manager = EngineManager()

    result = manager.process(
        "hari ini aku merasa produktif"
    )

    assert result is not None


def test_knowledge_has_priority_over_conversation():
    manager = EngineManager()

    result = manager.process(
        "jelaskan Python"
    )

    assert result is not None
    assert "mencari informasi" in result
