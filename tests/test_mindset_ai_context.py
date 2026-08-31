from core.context_builder import build_context


def test_build_context_detects_resilient_mindset():
    context = build_context(
        "Aku gagal lagi belajar Python dan ingin menyerah"
    )

    assert context.active_mindset is not None
    assert context.active_mindset.name == "resilient"