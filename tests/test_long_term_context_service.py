from core.domain.long_term_context import LongTermContext
from services.long_term_context_service import (
    aggregate_context,
    create_context,
    deduplicate_context,
    get_relevant_context,
    get_recent_context,
    get_stable_context,
    normalize_category,
    normalize_content,
)


def test_normalize_content():
    result = normalize_content("  Python   dan   Robotics  ")

    assert result == "Python dan Robotics"


def test_normalize_category():
    result = normalize_category("  SKILL ")

    assert result == "skill"


def test_create_context_normalizes_data():
    context = create_context(
        content="  Python   ",
        category=" SKILL ",
        source=" user_statement ",
        confidence=1.0,
        relevance=0.9,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    assert context.content == "Python"
    assert context.category == "skill"
    assert context.source == "user_statement"


def test_deduplicate_context():
    contexts = [
        LongTermContext(
            content="Python",
            category="skill",
            source="memory",
            confidence=1.0,
            relevance=0.9,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
        LongTermContext(
            content="python",
            category="skill",
            source="memory",
            confidence=0.8,
            relevance=0.8,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
    ]

    result = deduplicate_context(contexts)

    assert len(result) == 1


def test_get_stable_context():
    contexts = [
        LongTermContext(
            content="Python",
            category="skill",
            source="memory",
            confidence=1.0,
            relevance=0.9,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
        LongTermContext(
            content="Menyelesaikan project",
            category="goal",
            source="goal",
            confidence=1.0,
            relevance=0.9,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
    ]

    result = get_stable_context(contexts)

    assert len(result) == 1
    assert result[0].category == "skill"


def test_get_relevant_context():
    contexts = [
        LongTermContext(
            content="Python",
            category="skill",
            source="memory",
            confidence=1.0,
            relevance=0.9,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
        LongTermContext(
            content="Gaming",
            category="interest",
            source="memory",
            confidence=0.8,
            relevance=0.2,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
    ]

    result = get_relevant_context(contexts)

    assert len(result) == 1
    assert result[0].content == "Python"


def test_get_recent_context():
    contexts = [
        LongTermContext(
            content="Older",
            category="skill",
            source="memory",
            confidence=1.0,
            relevance=0.8,
            created_at="2026-08-19T00:00:00",
            updated_at="2026-08-19T00:00:00",
        ),
        LongTermContext(
            content="Newer",
            category="skill",
            source="memory",
            confidence=1.0,
            relevance=0.8,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        ),
    ]

    result = get_recent_context(contexts)

    assert result[0].content == "Newer"


def test_aggregate_context():
    contexts = [
        LongTermContext(
            content="  Python  ",
            category=" SKILL ",
            source="memory",
            confidence=1.0,
            relevance=0.9,
            created_at="2026-08-20T00:00:00",
            updated_at="2026-08-20T00:00:00",
        )
    ]

    result = aggregate_context(contexts)

    assert len(result) == 1
    assert result[0].content == "Python"
    assert result[0].category == "skill"