from core.context import AuraContext
from core.engines.mindset_engine import MindsetEngine


def test_mindset_engine_supports_context():
    engine = MindsetEngine()
    context = AuraContext("jelaskan mindset growth")

    result = engine.process_with_context(
        "jelaskan mindset growth",
        context,
    )

    assert result is not None
    assert "growth" in result