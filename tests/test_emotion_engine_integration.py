from core.engines.engine_manager import EngineManager


def test_engine_manager_handles_emotion_input():
    manager = EngineManager()

    result = manager.process(
        "Aku sedang cemas menghadapi ujian"
    )

    assert result == (
        "Aku menangkap bahwa kamu sedang merasa anxious."
    )


def test_emotion_engine_has_priority_over_conversation():
    manager = EngineManager()

    result = manager.process(
        "Aku sedang sedih hari ini"
    )

    assert result == (
        "Aku menangkap bahwa kamu sedang merasa sad."
    )