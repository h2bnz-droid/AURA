from unittest.mock import patch

from services.long_term_context_service import collect_long_term_context


@patch("services.long_term_context_service.owner_name")
@patch("services.long_term_context_service.recall_all")
@patch("services.long_term_context_service.active_goals")
@patch("services.long_term_context_service.latest")
@patch("services.long_term_context_service.get_all_relationships")
@patch("services.long_term_context_service.active_learning")
@patch("services.long_term_context_service.get_all")
def test_collect_long_term_context(
    mock_cognitive_model,
    mock_learning,
    mock_relationships,
    mock_reflections,
    mock_goals,
    mock_memories,
    mock_owner_name,
):
    mock_owner_name.return_value = "Budi"

    mock_memories.return_value = [
        {
            "memory_value": "Suka Python",
        }
    ]

    mock_goals.return_value = [
        {
            "title": "Membangun AURA",
            "category": "Technology",
            "status": "active",
            "priority": 1,
            "progress": 50,
            "created_at": "2026-08-20 00:00:00",
            "updated_at": "2026-08-20 00:00:00",
        }
    ]

    mock_reflections.return_value = [
        {
            "summary": "AURA perlu dikembangkan secara bertahap",
            "created_at": "2026-08-20 00:00:00",
        }
    ]

    mock_relationships.return_value = [
        {
            "person_name": "Budi",
            "relationship_type": "friend",
            "status": "active",
            "note": None,
            "created_at": "2026-08-20 00:00:00",
            "updated_at": "2026-08-20 00:00:00",
        }
    ]

    mock_learning.return_value = [
        {
            "topic": "Robotics",
            "status": "active",
            "progress": 25,
            "created_at": "2026-08-20 00:00:00",
            "updated_at": "2026-08-20 00:00:00",
        }
    ]

    mock_cognitive_model.return_value = [
        {
            "attribute_name": "career",
            "attribute_value": "Software Engineer",
            "category": "aspiration",
            "source": "user",
            "confidence": 1.0,
            "created_at": "2026-08-20 00:00:00",
            "updated_at": "2026-08-20 00:00:00",
        }
    ]

    result = collect_long_term_context()

    assert result
    assert any(
        context.content == "Budi"
        and context.category == "identity"
        for context in result
    )

    assert any(
        context.content == "Suka Python"
        for context in result
    )

    assert any(
        context.content == "Membangun AURA"
        and context.category == "goal"
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