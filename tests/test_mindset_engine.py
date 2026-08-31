from core.engines.mindset_engine import MindsetEngine


def test_mindset_engine_show():
    engine = MindsetEngine()

    result = engine.process("lihat mindset")

    assert result is not None
    assert "growth" in result


def test_mindset_engine_find():
    engine = MindsetEngine()

    result = engine.process("jelaskan mindset growth")

    assert result is not None
    assert "berkembang" in result


def test_mindset_engine_unknown():
    engine = MindsetEngine()

    assert engine.process("halo AURA") is None

def test_mindset_engine_sets_active_mindset_in_context():
    engine = MindsetEngine()

    context = type(
        "Context",
        (),
        {"active_mindset": None},
    )()

    result = engine.process_with_context(
        "jelaskan mindset growth",
        context,
    )

    assert result is not None
    assert context.active_mindset is not None
    assert context.active_mindset.name == "growth"

def test_mindset_engine_does_not_set_mindset_for_unrelated_message():
    engine = MindsetEngine()

    context = type(
        "Context",
        (),
        {"active_mindset": None},
    )()

    result = engine.process_with_context(
        "halo AURA",
        context,
    )

    assert result is None
    assert context.active_mindset is None