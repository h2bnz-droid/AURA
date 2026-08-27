from services.integrated_cognitive_context_service import (
    IntegratedCognitiveContextService,
)


def test_same_category_different_values_are_preserved():
    service = IntegratedCognitiveContextService()

    context = service.build(
        stable=[
            {
                "category": "preference",
                "value": "learning_by_practice",
                "source": "user_statement",
                "confidence": 1.0,
            },
            {
                "category": "preference",
                "value": "learning_by_reading",
                "source": "inference",
                "confidence": 0.72,
            },
        ]
    )

    assert len(context.stable) == 2


def test_duplicate_values_are_removed_case_insensitively():
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
                "category": "SKILL",
                "value": "python",
                "source": "inference",
                "confidence": 0.72,
            },
        ]
    )

    assert len(context.stable) == 1


def test_confidence_is_preserved():
    service = IntegratedCognitiveContextService()

    context = service.build(
        stable=[
            {
                "category": "preference",
                "value": "learning_by_practice",
                "source": "inference",
                "confidence": 0.72,
            }
        ]
    )

    item = context.stable[0]

    assert item.confidence == 0.72
    assert item.source == "inference"