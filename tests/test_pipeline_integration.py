from unittest.mock import patch

from core.router import process_user_input
from core.context import AuraContext
from core.chat import ask

@patch("core.chat.chat")
@patch("core.chat.add")
@patch("core.chat.build_context")
def test_chat_pipeline_integration(
    mock_build_context,
    mock_add,
    mock_chat,
):
    mock_chat.return_value = "Jawaban dari AURA"

    mock_context = AuraContext("ceritakan sesuatu")
    mock_context.profile = None
    mock_context.memories = []
    mock_context.history = []

    mock_build_context.return_value = mock_context

    result = ask("ceritakan sesuatu")

    assert result == "Jawaban dari AURA"

    mock_build_context.assert_called_once_with(
        "ceritakan sesuatu"
    )

    mock_chat.assert_called_once()

    assert mock_add.call_count == 2

@patch("core.router.engine_manager.process")
def test_pipeline_engine_has_priority(mock_engine):
    mock_engine.return_value = "Response dari engine"

    result = process_user_input("buat rencana belajar Python")

    assert result == "Response dari engine"

@patch("core.router.engine_manager.process")
@patch("core.router.detect_command")
@patch("core.router.recall_all")
def test_pipeline_command_after_engine(
    mock_recall_all,
    mock_detect_command,
    mock_engine,
):
    mock_engine.return_value = None
    mock_detect_command.return_value = "show_memory"
    mock_recall_all.return_value = "Memory AURA"

    result = process_user_input("lihat memory")

    assert result == "Memory AURA"

@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.detect_command")
@patch("core.router.engine_manager.process")
def test_ai_pipeline_fallback(
    mock_engine,
    mock_detect_command,
    mock_run,
    mock_ask,
):
    mock_engine.return_value = None
    mock_detect_command.return_value = None
    mock_run.return_value = None
    mock_ask.return_value = "Jawaban dari AURA"

    result = process_user_input("ceritakan sesuatu")

    assert result == "Jawaban dari AURA"
    mock_ask.assert_called_once_with("ceritakan sesuatu")
