from core.context_builder import (
    build_context,
    build_integrated_cognitive_context,
)
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)


def test_build_context_includes_integrated_cognitive_context(monkeypatch):
    expected = IntegratedCognitiveContext(
        stable=[
            CognitiveContextItem(
                category="skill",
                value="Python",
                source="user_statement",
                confidence=1.0,
            )
        ]
    )

    monkeypatch.setattr(
        "core.context_builder.build_integrated_cognitive_context",
        lambda user_input: expected,
    )

    context = build_context("Apa yang kamu tahu tentang saya?")

    assert context.integrated_cognitive_context is expected


def test_build_context_handles_empty_integrated_cognitive_context(monkeypatch):
    expected = IntegratedCognitiveContext()

    monkeypatch.setattr(
        "core.context_builder.build_integrated_cognitive_context",
        lambda user_input: expected,
    )

    context = build_context("Halo")

    assert context.integrated_cognitive_context is expected

def test_integrated_cognitive_context_marks_active_mindset():
    context = type(
        "Context",
        (),
        {
            "active_mindset": type(
                "Mindset",
                (),
                {
                    "name": "growth",
                    "description": "Kemampuan dapat berkembang.",
                },
            )(),
        },
    )()

    result = build_integrated_cognitive_context("belajar")

    items = result.all_items()

    assert any(
        item.category == "mindset"
        and item.value == "growth"
        for item in items
    )

def test_integrated_cognitive_context_uses_active_mindset():
    result = build_integrated_cognitive_context("jelaskan mindset growth")

    items = result.all_items()

    mindset_values = [
        item.value
        for item in items
        if item.category == "mindset"
    ]

    assert "growth" in mindset_values