from core.context_builder import build_context


def test_mindsets_are_in_integrated_cognitive_context():
    context = build_context("belajar Python")

    items = context.integrated_cognitive_context.all_items()

    assert any(
        item.category == "mindset"
        and item.value == "growth"
        for item in items
    )