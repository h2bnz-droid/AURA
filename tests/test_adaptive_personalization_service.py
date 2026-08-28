from core.domain.personalization import (
    PersonalizationPreference,
    PersonalizationSignal,
)
from services.adaptive_personalization_service import (
    AdaptivePersonalizationService,
)


def test_service_saves_preference():
    service = AdaptivePersonalizationService()

    preference = PersonalizationPreference(
        name="response_style",
        value="casual",
        source="user_statement",
        confidence=1.0,
        created_at="",
        updated_at="",
    )

    service.save_preference(preference)

    assert service.get_preferences() == [preference]


def test_service_stores_signal():
    service = AdaptivePersonalizationService()

    signal = PersonalizationSignal(
        name="explanation_style",
        value="step_by_step",
        source="interaction_pattern",
        confidence=0.82,
        timestamp="",
    )

    service.add_signal(signal)

    assert service.get_signals() == [signal]


def test_service_filters_low_confidence_signals():
    service = AdaptivePersonalizationService()

    high = PersonalizationSignal(
        name="response_style",
        value="casual",
        source="interaction_pattern",
        confidence=0.9,
        timestamp="",
    )

    low = PersonalizationSignal(
        name="explanation_style",
        value="detailed",
        source="interaction_pattern",
        confidence=0.4,
        timestamp="",
    )

    service.add_signal(high)
    service.add_signal(low)

    result = service.get_high_confidence_signals()

    assert result == [high]

def test_service_builds_personalization_context():
    service = AdaptivePersonalizationService()

    preference = PersonalizationPreference(
        name="response_style",
        value="casual",
        source="user_statement",
        confidence=1.0,
        created_at="",
        updated_at="",
    )

    service.save_preference(preference)

    context = service.build_context()

    assert context["response_style"] == "casual"

def test_new_preference_replaces_existing_preference():
    service = AdaptivePersonalizationService()

    first = PersonalizationPreference(
        name="response_style",
        value="formal",
        source="user_statement",
        confidence=1.0,
        created_at="2026-01-01",
        updated_at="2026-01-01",
    )

    second = PersonalizationPreference(
        name="response_style",
        value="casual",
        source="user_statement",
        confidence=1.0,
        created_at="2026-01-02",
        updated_at="2026-01-02",
    )

    service.save_preference(first)
    service.save_preference(second)

    context = service.build_context()

    assert context["response_style"] == "casual"

def test_low_confidence_signal_is_not_used_in_context():
    service = AdaptivePersonalizationService()

    signal = PersonalizationSignal(
        name="response_style",
        value="formal",
        source="interaction_pattern",
        confidence=0.4,
        timestamp="2026-01-01",
    )

    service.add_signal(signal)

    context = service.build_context()

    assert "response_style" not in context

def test_high_confidence_signal_is_used_in_context():
    service = AdaptivePersonalizationService()

    signal = PersonalizationSignal(
        name="explanation_style",
        value="step_by_step",
        source="interaction_pattern",
        confidence=0.9,
        timestamp="2026-01-01",
    )

    service.add_signal(signal)

    context = service.build_context()

    assert context["explanation_style"] == "step_by_step"

def test_preference_has_priority_over_high_confidence_signal():
    service = AdaptivePersonalizationService()

    preference = PersonalizationPreference(
        name="response_style",
        value="casual",
        source="user_statement",
        confidence=1.0,
        created_at="2026-01-01",
        updated_at="2026-01-01",
    )

    signal = PersonalizationSignal(
        name="response_style",
        value="formal",
        source="interaction_pattern",
        confidence=0.95,
        timestamp="2026-01-02",
    )

    service.save_preference(preference)
    service.add_signal(signal)

    context = service.build_context()

    assert context["response_style"] == "casual"

def test_latest_high_confidence_signal_wins():
    service = AdaptivePersonalizationService()

    first = PersonalizationSignal(
        name="explanation_style",
        value="short",
        source="interaction_pattern",
        confidence=0.9,
        timestamp="2026-01-01",
    )

    second = PersonalizationSignal(
        name="explanation_style",
        value="step_by_step",
        source="interaction_pattern",
        confidence=0.9,
        timestamp="2026-01-02",
    )

    service.add_signal(first)
    service.add_signal(second)

    context = service.build_context()

    assert context["explanation_style"] == "step_by_step"
