from unittest.mock import patch

from core.context_builder import build_context
from core.prompt_builder import PromptBuilder


@patch("core.context_builder.collect_long_term_context")
def test_long_term_context_flows_into_prompt(
    mock_collect_long_term_context,
):
    mock_collect_long_term_context.return_value = [
        {
            "content": "Software Engineer",
            "category": "aspiration",
            "source": "personal_cognitive_model",
        }
    ]

    context = build_context(
        "Aku ingin membangun karier di bidang software."
    )

    prompt = PromptBuilder().build(context)

    assert context.long_term_context
    assert "[LONG-TERM CONTEXT]" in prompt
    assert "Software Engineer" in prompt
    assert "Aku ingin membangun karier di bidang software." in prompt