from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_includes_personalization_context():
    context = AuraContext("jelaskan ini")

    context.personalization = {
        "response_style": "casual",
        "explanation_style": "step_by_step",
    }

    prompt = PromptBuilder().build(context)

    assert "[PERSONALIZATION]" in prompt
    assert "- response_style: casual" in prompt
    assert "- explanation_style: step_by_step" in prompt

def test_prompt_omits_empty_personalization_context():
    context = AuraContext("hello")

    context.personalization = {}

    prompt = PromptBuilder().build(context)

    assert "[PERSONALIZATION]" not in prompt
