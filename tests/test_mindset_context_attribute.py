from core.context_builder import build_context


def test_build_context_includes_mindsets():
    context = build_context("belajar Python")

    assert hasattr(context, "mindsets")
    assert len(context.mindsets) == 3
    assert any(
        mindset.name == "growth"
        for mindset in context.mindsets
    )