from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_includes_reflection_context():
    context = AuraContext(
        "Apa yang bisa aku pelajari dari pengalaman ini?"
    )

    context.reflections = [
        {
            "summary": "Aku belajar bahwa konsistensi lebih penting.",
            "insights": "Konsistensi",
            "questions": "Apa yang bisa diperbaiki?",
        }
    ]

    prompt = PromptBuilder().build(context)

    assert "[REFLECTION]" in prompt
    assert "Aku belajar bahwa konsistensi lebih penting." in prompt
