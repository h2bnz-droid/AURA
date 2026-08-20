from core.context_builder import build_context
from services.cognitive_model_service import save


def test_context_loads_cognitive_model():
    save(
        attribute_name="skill",
        attribute_value="Python",
        category="skill",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    context = build_context("apa kemampuan saya?")

    assert len(context.cognitive_model) > 0
    assert context.cognitive_model[0]["attribute_name"] == "skill"

def test_context_contains_cognitive_model():
    context = build_context("apa yang kamu tahu tentang saya?")

    assert hasattr(context, "cognitive_model")
    assert context.cognitive_model is not None