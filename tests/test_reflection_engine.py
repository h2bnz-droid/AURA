from core.domain.reflection_intent import ReflectionIntent
from core.engines.reflection_engine import ReflectionEngine


def test_reflection_engine_detects_reflect():
    engine = ReflectionEngine()

    result = engine.analyze(
        "Aku ingin merenung"
    )

    assert result == ReflectionIntent.REFLECT


def test_reflection_engine_detects_show_reflections():
    engine = ReflectionEngine()

    result = engine.analyze(
        "Lihat refleksi saya"
    )

    assert result == ReflectionIntent.SHOW_REFLECTIONS


def test_reflection_engine_returns_unknown():
    engine = ReflectionEngine()

    result = engine.analyze(
        "Halo AURA"
    )

    assert result == ReflectionIntent.UNKNOWN_INTENT
