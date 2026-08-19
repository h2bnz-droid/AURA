from core.domain.reflection_intent import ReflectionIntent


def test_reflection_intent_values():
    assert ReflectionIntent.REFLECT
    assert ReflectionIntent.SHOW_REFLECTIONS
    assert ReflectionIntent.UNKNOWN_INTENT