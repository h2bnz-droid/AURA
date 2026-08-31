from core.context_builder import build_context


def test_context_detects_growth_mindset():
    context = build_context(
        "Aku ingin meningkatkan kemampuan Python"
    )

    assert context.active_mindset is not None
    assert context.active_mindset.name == "growth"


def test_context_detects_resilient_mindset():
    context = build_context(
        "Aku gagal lagi dan ingin menyerah"
    )

    assert context.active_mindset is not None
    assert context.active_mindset.name == "resilient"


def test_context_has_no_active_mindset_when_unknown():
    context = build_context("Halo AURA")

    assert context.active_mindset is None