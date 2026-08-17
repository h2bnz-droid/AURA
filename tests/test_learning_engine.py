from unittest.mock import patch
from database.learning import create_table
from core.domain.learning_intent import LearningIntent
from core.engines.learning_engine import LearningEngine

create_table()

@patch("core.engines.learning_engine.start_learning")
def test_learning_engine_saves_learning(mock_start):
    engine = LearningEngine()

    result = engine.process(
        "Aku sedang belajar Python"
    )

    mock_start.assert_called_once_with("Python")
    assert result == "Aku akan mencatat proses belajarmu."


def test_learning_engine_detects_learning_progress():
    engine = LearningEngine()

    result = engine.analyze(
        "Progress Python 50%"
    )

    assert result == LearningIntent.PROGRESS


def test_learning_engine_detects_show_learning():
    engine = LearningEngine()

    result = engine.analyze(
        "Apa yang sedang kupelajari?"
    )

    assert result == LearningIntent.SHOW


def test_learning_engine_returns_unknown():
    engine = LearningEngine()

    result = engine.analyze(
        "Halo AURA"
    )

    assert result == LearningIntent.UNKNOWN


def test_learning_engine_process_start():
    engine = LearningEngine()

    result = engine.process(
        "Aku sedang belajar Python"
    )

    assert result == "Aku akan mencatat proses belajarmu."


def test_learning_engine_process_show():
    engine = LearningEngine()

    result = engine.process(
        "Apa yang sedang kupelajari?"
    )

    assert result == "Aku akan menampilkan pembelajaranmu."


def test_learning_engine_process_unknown():
    engine = LearningEngine()

    result = engine.process(
        "Halo AURA"
    )

    assert result is None

@patch("core.engines.learning_engine.update_learning_progress")
def test_learning_engine_updates_progress(mock_update):
    engine = LearningEngine()

    result = engine.process(
        "Progress Python 50%"
    )

    mock_update.assert_called_once_with("Python", 50)
    assert result == "Aku akan mencatat progress belajarmu."

@patch("core.engines.learning_engine.active_learning")
def test_learning_engine_process_show(mock_active):
    mock_active.return_value = [
        {
            "topic": "Python",
            "progress": 50,
        },
        {
            "topic": "Machine Learning",
            "progress": 20,
        },
    ]

    engine = LearningEngine()

    result = engine.process(
        "Apa yang sedang kupelajari?"
    )

    mock_active.assert_called_once()

    assert "Python" in result
    assert "50%" in result
    assert "Machine Learning" in result
    assert "20%" in result    

@patch("core.engines.learning_engine.active_learning")
def test_learning_engine_process_show_empty(mock_active):
    mock_active.return_value = []

    engine = LearningEngine()

    result = engine.process(
        "Apa yang sedang kupelajari?"
    )

    mock_active.assert_called_once()

    assert result == "Belum ada pembelajaran aktif."    

@patch("core.engines.learning_engine.start_learning")
def test_learning_engine_process_start(mock_start):
    engine = LearningEngine()

    result = engine.process("Aku sedang belajar Python")

    mock_start.assert_called_once_with("Python")
    assert result == "Aku akan mencatat proses belajarmu."    