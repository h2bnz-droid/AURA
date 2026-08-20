from core.domain.long_term_context import LongTermContext
from services.cognitive_model_service import save as save_cognitive_model
from services.goal_service import add_goal
from services.learning_service import start_learning
from services.long_term_context_service import collect_long_term_context
from services.profile_service import create_profile
from services.relationship_service import save_relationship


def test_collect_long_term_context_from_real_services():
    create_profile("AURA Test User")

    add_goal(
        title="Membangun AURA",
        description="Develop AURA cognitive assistant",
        category="Technology",
        priority=1,
    )

    save_relationship(
        person_name="Budi",
        relationship_type="friend",
    )

    start_learning("Robotics")

    save_cognitive_model(
        attribute_name="career",
        attribute_value="Software Engineer",
        category="aspiration",
        source="user",
        confidence=1.0,
        created_at="2026-08-20 00:00:00",
        updated_at="2026-08-20 00:00:00",
    )

    result = collect_long_term_context()

    assert result
    assert all(
        isinstance(context, LongTermContext)
        for context in result
    )

    assert any(
        context.content == "AURA Test User"
        and context.category == "identity"
        for context in result
    )

    assert any(
        context.content == "Membangun AURA"
        and context.category == "goal"
        for context in result
    )

    assert any(
        context.content == "Budi"
        and context.category == "relationship"
        for context in result
    )

    assert any(
        context.content == "Robotics"
        and context.category == "learning"
        for context in result
    )

    assert any(
        context.content == "Software Engineer"
        and context.category == "aspiration"
        for context in result
    )