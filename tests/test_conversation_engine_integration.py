from core.engines.conversation_engine import ConversationEngine
from core.engines.engine_manager import EngineManager


def test_engine_manager_contains_conversation_engine():
    manager = EngineManager()

    assert any(
        isinstance(engine, ConversationEngine)
        for engine in manager.engines
    )


def test_engine_manager_handles_greeting():
    manager = EngineManager()

    result = manager.process(
        "Halo AURA"
    )

    assert result == "Halo! Ada yang bisa aku bantu?"


def test_engine_manager_handles_chat():
    manager = EngineManager()

    result = manager.process(
        "Hari ini aku sedang merasa cukup produktif"
    )

    assert result is not None
    assert "mendengarkan" in result


def test_engine_manager_handles_empty_message():
    manager = EngineManager()

    result = manager.process("")

    assert result is None