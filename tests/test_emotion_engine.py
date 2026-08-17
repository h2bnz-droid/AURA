from unittest.mock import patch

from core.domain.emotion_intent import EmotionIntent
from core.engines.emotion_engine import EmotionEngine


def test_emotion_engine_detects_happy():
    engine = EmotionEngine()

    result = engine.analyze(
        "Aku sangat senang hari ini"
    )

    assert result == EmotionIntent.DETECT


def test_emotion_engine_detects_sad():
    engine = EmotionEngine()

    result = engine.analyze(
        "Aku sedang sedih"
    )

    assert result == EmotionIntent.DETECT


def test_emotion_engine_detects_anxious():
    engine = EmotionEngine()

    result = engine.analyze(
        "Aku merasa cemas menghadapi besok"
    )

    assert result == EmotionIntent.DETECT


def test_emotion_engine_detects_show():
    engine = EmotionEngine()

    result = engine.analyze(
        "Apa emosiku?"
    )

    assert result == EmotionIntent.SHOW


def test_emotion_engine_detects_track():
    engine = EmotionEngine()

    result = engine.analyze(
        "Bagaimana perasaanku?"
    )

    assert result == EmotionIntent.TRACK


def test_emotion_engine_unknown():
    engine = EmotionEngine()

    result = engine.analyze(
        "Berapa harga laptop?"
    )

    assert result == EmotionIntent.UNKNOWN


@patch("core.engines.emotion_engine.record_emotion")
def test_emotion_engine_saves_detected_emotion(mock_record):
    engine = EmotionEngine()

    result = engine.process(
        "Aku sangat senang hari ini"
    )

    mock_record.assert_called_once_with(
        "happy",
        0.5,
        "user_message",
    )

    assert result == (
        "Aku menangkap bahwa kamu sedang merasa happy."
    )


def test_emotion_engine_process_unknown():
    engine = EmotionEngine()

    result = engine.process(
        "Berapa harga laptop?"
    )

    assert result is None