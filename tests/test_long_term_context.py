from core.domain.long_term_context import LongTermContext


def test_long_term_context_creation():
    context = LongTermContext(
        content="User memiliki kemampuan Python",
        category="skill",
        source="personal_cognitive_model",
        confidence=1.0,
        relevance=0.9,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    assert context.content == "User memiliki kemampuan Python"
    assert context.category == "skill"
    assert context.source == "personal_cognitive_model"
    assert context.confidence == 1.0
    assert context.relevance == 0.9


def test_long_term_context_supports_different_sources():
    context = LongTermContext(
        content="User sedang belajar robotics",
        category="learning",
        source="learning",
        confidence=0.8,
        relevance=0.7,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    assert context.source == "learning"
    assert context.category == "learning"