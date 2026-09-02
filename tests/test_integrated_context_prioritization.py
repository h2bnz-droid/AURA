from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)
from services.context_prioritization_service import (
    ContextPrioritizationService,
)


def test_prioritize_integrated_cognitive_context_items():
    context = IntegratedCognitiveContext(
        stable=[
            CognitiveContextItem(
                category="memory",
                value="User suka Python",
                source="memory_service",
                confidence=1.0,
            )
        ],
        relevant=[
            CognitiveContextItem(
                category="mindset",
                value="growth",
                source="mindset_service",
                confidence=1.0,
            )
        ],
        recent=[
            CognitiveContextItem(
                category="emotion",
                value="focused",
                source="cognitive_state",
                confidence=1.0,
            )
        ],
    )

    service = ContextPrioritizationService()

    result = service.prioritize(
        context.all_items()
    )

    assert result[0].category == "mindset"
    assert result[1].category == "emotion"
    assert result[2].category == "memory"


def test_prioritize_preserves_integrated_context_metadata():
    item = CognitiveContextItem(
        category="mindset",
        value="growth",
        source="mindset_service",
        confidence=0.9,
        relevance=0.8,
    )

    service = ContextPrioritizationService()

    result = service.prioritize([item])

    assert result[0].source == "mindset_service"
    assert result[0].confidence == 0.9
    assert result[0].relevance == 0.8


def test_prioritize_integrated_context_with_limit():
    context = IntegratedCognitiveContext(
        stable=[
            CognitiveContextItem(
                category="memory",
                value="Python",
                source="memory_service",
                confidence=1.0,
            )
        ],
        relevant=[
            CognitiveContextItem(
                category="mindset",
                value="growth",
                source="mindset_service",
                confidence=1.0,
            )
        ],
        recent=[
            CognitiveContextItem(
                category="emotion",
                value="focused",
                source="cognitive_state",
                confidence=1.0,
            )
        ],
    )

    service = ContextPrioritizationService()

    result = service.prioritize(
        context.all_items(),
        limit=2,
    )

    assert len(result) == 2
    assert result[0].category == "mindset"
    assert result[1].category == "emotion"