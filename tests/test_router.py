from unittest.mock import patch

from core.router import process_user_input


@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.owner_name")
@patch("core.router.recall_all")
@patch("core.router.detect_command")
@patch("core.router.engine_manager")
def test_engine_response_has_priority(
    mock_engine_manager,
    mock_detect_command,
    mock_recall_all,
    mock_owner_name,
    mock_run,
    mock_ask,
):
    mock_engine_manager.process.return_value = "Jawaban dari engine"

    result = process_user_input("buat rencana untuk belajar Python")

    assert result == "Jawaban dari engine"

    mock_engine_manager.process.assert_called_once_with(
        "buat rencana untuk belajar Python"
    )

    mock_detect_command.assert_not_called()
    mock_run.assert_not_called()
    mock_ask.assert_not_called()


@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.owner_name")
@patch("core.router.recall_all")
@patch("core.router.detect_command")
@patch("core.router.engine_manager")
def test_show_memory_command(
    mock_engine_manager,
    mock_detect_command,
    mock_recall_all,
    mock_owner_name,
    mock_run,
    mock_ask,
):
    mock_engine_manager.process.return_value = None
    mock_detect_command.return_value = "show_memory"
    mock_recall_all.return_value = "Memory AURA"

    result = process_user_input("tampilkan memory")

    assert result == "Memory AURA"
    mock_recall_all.assert_called_once()

    mock_owner_name.assert_not_called()
    mock_run.assert_not_called()
    mock_ask.assert_not_called()


@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.owner_name")
@patch("core.router.recall_all")
@patch("core.router.detect_command")
@patch("core.router.engine_manager")
def test_who_am_i_command(
    mock_engine_manager,
    mock_detect_command,
    mock_recall_all,
    mock_owner_name,
    mock_run,
    mock_ask,
):
    mock_engine_manager.process.return_value = None
    mock_detect_command.return_value = "who_am_i"
    mock_owner_name.return_value = "Hibban"

    result = process_user_input("siapa saya")

    assert result == "Nama Anda adalah Hibban."

    mock_owner_name.assert_called_once()
    mock_run.assert_not_called()
    mock_ask.assert_not_called()


@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.owner_name")
@patch("core.router.recall_all")
@patch("core.router.detect_command")
@patch("core.router.engine_manager")
def test_skill_response(
    mock_engine_manager,
    mock_detect_command,
    mock_recall_all,
    mock_owner_name,
    mock_run,
    mock_ask,
):
    mock_engine_manager.process.return_value = None
    mock_detect_command.return_value = None
    mock_run.return_value = "Hasil skill"

    result = process_user_input("hitung 2 + 2")

    assert result == "Hasil skill"
    mock_run.assert_called_once_with("hitung 2 + 2")
    mock_ask.assert_not_called()


@patch("core.router.ask")
@patch("core.router.run")
@patch("core.router.owner_name")
@patch("core.router.recall_all")
@patch("core.router.detect_command")
@patch("core.router.engine_manager")
def test_ai_fallback(
    mock_engine_manager,
    mock_detect_command,
    mock_recall_all,
    mock_owner_name,
    mock_run,
    mock_ask,
):
    mock_engine_manager.process.return_value = None
    mock_detect_command.return_value = None
    mock_run.return_value = None
    mock_ask.return_value = "Jawaban AI"

    result = process_user_input("jelaskan relativitas")

    assert result == "Jawaban AI"
    mock_ask.assert_called_once_with("jelaskan relativitas")
