from core.domain.temporal_intent import TemporalIntent


def test_temporal_intent_values():
    assert TemporalIntent.TREND.value == "trend"
    assert TemporalIntent.HISTORY.value == "history"
    assert TemporalIntent.STATE.value == "state"
    assert TemporalIntent.UNKNOWN.value == "unknown"