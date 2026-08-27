from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)


def test_cognitive_context_item_creation():
    item = CognitiveContextItem(
        category="skill",
        value="Python",
        source="user_statement",
        confidence=1.0,
        relevance=1.0,
    )

    assert item.category == "skill"
    assert item.value == "Python"
    assert item.source == "user_statement"
    assert item.confidence == 1.0
    assert item.relevance == 1.0


def test_integrated_cognitive_context_creation():
    item = CognitiveContextItem(
        category="preference",
        value="learning_by_practice",
        source="inference",
        confidence=0.72,
        relevance=0.8,
    )

    context = IntegratedCognitiveContext(
        stable=[item]
    )

    assert len(context.stable) == 1
    assert context.stable[0].value == "learning_by_practice"


def test_all_items_combines_context_layers():
    stable = CognitiveContextItem(
        category="identity",
        value="developer",
        source="user_statement",
        confidence=1.0,
    )

    relevant = CognitiveContextItem(
        category="goal",
        value="build AURA",
        source="goal",
        confidence=1.0,
    )

    recent = CognitiveContextItem(
        category="reflection",
        value="Sprint 010 completed",
        source="reflection",
        confidence=1.0,
    )

    context = IntegratedCognitiveContext(
        stable=[stable],
        relevant=[relevant],
        recent=[recent],
    )

    items = context.all_items()

    assert len(items) == 3
    assert items[0].value == "developer"
    assert items[1].value == "build AURA"
    assert items[2].value == "Sprint 010 completed"