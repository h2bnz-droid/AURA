from unittest.mock import patch

from core.domain.temporal_intent import TemporalIntent
from core.engines.temporal_engine import TemporalEngine


def test_temporal_engine_detects_trend():
    engine = TemporalEngine()

    result = engine.analyze(
        "Bagaimana trend Python?"
    )

    assert result == TemporalIntent.TREND


def test_temporal_engine_detects_history():
    engine = TemporalEngine()

    result = engine.analyze(
        "Tampilkan riwayat Python"
    )

    assert result == TemporalIntent.HISTORY


def test_temporal_engine_detects_state():
    engine = TemporalEngine()

    result = engine.analyze(
        "Bagaimana kondisi saya?"
    )

    assert result == TemporalIntent.STATE


def test_temporal_engine_unknown():
    engine = TemporalEngine()

    result = engine.analyze(
        "Halo AURA"
    )

    assert result == TemporalIntent.UNKNOWN


@patch("core.engines.temporal_engine.event_history")
@patch("core.engines.temporal_engine.calculate_trend")
def test_temporal_engine_process_trend(
    mock_trend,
    mock_history,
):
    mock_history.return_value = [
        {"value": "20"},
        {"value": "50"},
    ]

    mock_trend.return_value = "increasing"

    engine = TemporalEngine()

    result = engine.process(
        "trend Python"
    )

    mock_history.assert_called_once_with(
        subject="Python",
    )

    mock_trend.assert_called_once_with(
        [20.0, 50.0],
    )

    assert result == "Trend Python sedang meningkat."


@patch("core.engines.temporal_engine.event_history")
def test_temporal_engine_process_history(
    mock_history,
):
    mock_history.return_value = [
        {"value": "20"},
        {"value": "50"},
    ]

    engine = TemporalEngine()

    result = engine.process(
        "riwayat Python"
    )

    assert "- 20" in result
    assert "- 50" in result


@patch("core.engines.temporal_engine.latest_event")
def test_temporal_engine_process_state(
    mock_latest,
):
    mock_latest.return_value = {
        "value": "happy"
    }

    engine = TemporalEngine()

    result = engine.process(
        "Bagaimana kondisi saya?"
    )

    assert result == (
        "Kondisi terakhir yang tercatat: happy."
    )


def test_temporal_engine_process_unknown():
    engine = TemporalEngine()

    result = engine.process(
        "Halo AURA"
    )

    assert result is None