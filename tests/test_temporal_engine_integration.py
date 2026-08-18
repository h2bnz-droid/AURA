from unittest.mock import patch

from core.engines.engine_manager import EngineManager


@patch(
    "core.engines.temporal_engine.event_history"
)
def test_engine_manager_handles_temporal_input(
    mock_history,
):
    mock_history.return_value = [
        {"value": "20"},
        {"value": "50"},
    ]

    manager = EngineManager()

    result = manager.process(
        "trend Python"
    )

    assert result == "Trend Python sedang meningkat."


def test_engine_manager_keeps_conversation_fallback():
    manager = EngineManager()

    result = manager.process(
        "Halo AURA"
    )

    assert result is not None