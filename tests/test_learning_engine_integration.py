from core.engines.engine_manager import EngineManager


def test_engine_manager_handles_learning_input():
    manager = EngineManager()

    result = manager.process(
        "Aku sedang belajar Python"
    )

    assert result == "Aku akan mencatat proses belajarmu."

def test_learning_does_not_capture_knowledge_question():
    manager = EngineManager()

    result = manager.process(
        "jelaskan Python"
    )

    assert result is not None
    assert "mencatat proses belajarmu" not in result

def test_learning_does_not_capture_general_conversation():
    manager = EngineManager()

    result = manager.process(
        "Halo AURA"
    )

    assert result is not None
    assert "mencatat proses belajarmu" not in result 

def test_learning_engine_has_priority_for_learning_input():
    manager = EngineManager()

    result = manager.process(
        "Aku sedang belajar Python"
    )

    assert result == "Aku akan mencatat proses belajarmu."           