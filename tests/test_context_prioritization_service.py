from core.domain.context_priority import ContextPriority
from services.context_prioritization_service import (
    ContextPrioritizationService,
)
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
)


def test_prioritize_orders_highest_priority_first():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="history",
            value="Halo",
            priority=0.0,
        ),
        ContextPriority(
            category="emotion",
            value="anxious",
            priority=0.0,
        ),
        ContextPriority(
            category="active_mindset",
            value="resilient",
            priority=0.0,
        ),
    ]

    result = service.prioritize(items)

    assert result[0].category == "active_mindset"
    assert result[1].category == "emotion"
    assert result[2].category == "history"


def test_prioritize_assigns_default_priority():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="memory",
            value="User suka Python",
            priority=0.0,
        )
    ]

    result = service.prioritize(items)

    assert result[0].priority == 0.85


def test_prioritize_unknown_category_uses_zero_priority():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="unknown",
            value="test",
            priority=0.0,
        )
    ]

    result = service.prioritize(items)

    assert result[0].priority == 0.0

def test_prioritize_removes_duplicate_context():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="memory",
            value="User suka Python",
            priority=0.0,
        ),
        ContextPriority(
            category="memory",
            value="User suka Python",
            priority=0.0,
        ),
    ]

    result = service.prioritize(items)

    assert len(result) == 1


def test_prioritize_respects_limit():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="history",
            value="Halo",
            priority=0.0,
        ),
        ContextPriority(
            category="emotion",
            value="anxious",
            priority=0.0,
        ),
        ContextPriority(
            category="active_mindset",
            value="resilient",
            priority=0.0,
        ),
    ]

    result = service.prioritize(
        items,
        limit=2,
    )

    assert len(result) == 2
    assert result[0].category == "active_mindset"
    assert result[1].category == "emotion"

def test_prioritize_preserves_context_metadata():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="memory",
            value="User suka Python",
            priority=0.0,
            source="memory_service",
            confidence=0.9,
            relevance=0.8,
        )
    ]

    result = service.prioritize(items)

    assert result[0].source == "memory_service"
    assert result[0].confidence == 0.9
    assert result[0].relevance == 0.8

def test_prioritize_uses_default_limit():
    service = ContextPrioritizationService()

    items = [
        ContextPriority(
            category="memory",
            value=f"Memory {index}",
            priority=0.0,
        )
        for index in range(15)
    ]

    result = service.prioritize(items)

    assert len(result) == service.DEFAULT_LIMIT

def test_prioritize_all_does_not_apply_default_limit():
    service = ContextPrioritizationService()

    items = [
        CognitiveContextItem(
            category="memory",
            value=f"Memory {index}",
            source="memory_service",
            confidence=1.0,
        )
        for index in range(15)
    ]

    result = service.prioritize_all(items)

    assert len(result) == 15