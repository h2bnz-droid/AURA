from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
)
from services.integrated_cognitive_context_service import (
    IntegratedCognitiveContextService,
)


def test_service_builds_integrated_context():
    service = IntegratedCognitiveContextService()

    context = service.build(
        stable=[
            CognitiveContextItem(
                category="skill",
                value="Python",
                source="user_statement",
                confidence=1.0,
            )
        ],
        relevant=[
            CognitiveContextItem(
                category="goal",
                value="Build AURA",
                source="goal",
                confidence=1.0,
            )
        ],
        recent=[],
    )

    assert len(context.stable) == 1
    assert len(context.relevant) == 1


def test_service_normalizes_dictionary_items():
    service = IntegratedCognitiveContextService()

    context = service.build(
        stable=[
            {
                "category": " Skill ",
                "value": " Python ",
                "source": " user_statement ",
                "confidence": 1.0,
                "relevance": 0.8,
            }
        ]
    )

    item = context.stable[0]

    assert item.category == "skill"
    assert item.value == " Python "
    assert item.source == "user_statement"
    assert item.confidence == 1.0
    assert item.relevance == 0.8


def test_service_removes_duplicate_context():
    service = IntegratedCognitiveContextService()

    context = service.build(
        stable=[
            {
                "category": "skill",
                "value": "Python",
                "source": "user_statement",
                "confidence": 1.0,
            },
            {
                "category": "skill",
                "value": "python",
                "source": "inference",
                "confidence": 0.7,
            },
        ]
    )

    assert len(context.stable) == 1


def test_service_handles_empty_context():
    service = IntegratedCognitiveContextService()

    context = service.build()

    assert context.stable == []
    assert context.relevant == []
    assert context.recent == []
    assert context.all_items() == []