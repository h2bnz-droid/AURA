from unittest.mock import patch

from core.context_builder import build_context


@patch("core.context_builder.collect_long_term_context")
def test_build_context_includes_long_term_context(
    mock_collect_long_term_context,
):
    mock_collect_long_term_context.return_value = [
        {
            "content": "Software Engineer",
            "category": "aspiration",
            "source": "personal_cognitive_model",
        }
    ]

    context = build_context("Apa tujuan karierku?")

    assert hasattr(context, "long_term_context")
    assert context.long_term_context

    assert context.long_term_context[0]["content"] == "Software Engineer"
    assert context.long_term_context[0]["category"] == "aspiration"


@patch("core.context_builder.collect_long_term_context")
def test_build_context_handles_empty_long_term_context(
    mock_collect_long_term_context,
):
    mock_collect_long_term_context.return_value = []

    context = build_context("Halo")

    assert hasattr(context, "long_term_context")
    assert context.long_term_context == []