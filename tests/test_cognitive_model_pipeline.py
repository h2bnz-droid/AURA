from core.context_builder import build_context
from core.prompt_builder import PromptBuilder
from services.cognitive_model_service import save


def test_cognitive_model_pipeline():
    save(
        attribute_name="skill",
        attribute_value="Python",
        category="skill",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    context = build_context(
        "Apa kemampuan yang kamu ketahui tentang saya?"
    )

    assert hasattr(context, "cognitive_model")
    assert context.cognitive_model

    prompt = PromptBuilder().build(context)

    assert "[PERSONAL COGNITIVE MODEL]" in prompt
    assert "skill: Python" in prompt
    assert "CURRENT USER MESSAGE" in prompt
    assert "Apa kemampuan yang kamu ketahui tentang saya?" in prompt