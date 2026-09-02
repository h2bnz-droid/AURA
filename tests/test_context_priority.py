from core.domain.context_priority import ContextPriority


def test_context_priority_creation():
    item = ContextPriority(
        category="emotion",
        value="anxious",
        priority=0.9,
        source="emotion_service",
    )

    assert item.category == "emotion"
    assert item.value == "anxious"
    assert item.priority == 0.9
    assert item.source == "emotion_service"


def test_context_priority_source_defaults_to_none():
    item = ContextPriority(
        category="mindset",
        value="resilient",
        priority=1.0,
    )

    assert item.source is None