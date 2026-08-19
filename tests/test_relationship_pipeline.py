from core.context_builder import build_context
from core.prompt_builder import PromptBuilder
from core.engines.engine_manager import EngineManager


def test_relationship_pipeline():
    engine_manager = EngineManager()

    response = engine_manager.process(
        "Aku punya teman bernama Budi"
    )

    assert response is not None
    assert "Budi" in response

    context = build_context("lihat relasi")

    assert context.relationships

    prompt = PromptBuilder().build(context)

    assert "[RELATIONSHIP]" in prompt
    assert "Budi" in prompt
    assert "friend" in prompt