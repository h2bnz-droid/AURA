from core.domain.personalization import (
    PersonalizationPreference,
    PersonalizationSignal,
)


def test_personalization_preference_creation():
    preference = PersonalizationPreference(
        name="response_style",
        value="casual",
        source="user_statement",
        confidence=1.0,
        created_at="",
        updated_at="",
    )

    assert preference.name == "response_style"
    assert preference.value == "casual"
    assert preference.source == "user_statement"
    assert preference.confidence == 1.0


def test_personalization_signal_creation():
    signal = PersonalizationSignal(
        name="explanation_style",
        value="step_by_step",
        source="interaction_pattern",
        confidence=0.82,
        timestamp="",
    )

    assert signal.name == "explanation_style"
    assert signal.value == "step_by_step"
    assert signal.source == "interaction_pattern"
    assert signal.confidence == 0.82