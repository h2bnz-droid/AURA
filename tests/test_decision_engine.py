from core.domain.decision_intent import DecisionIntent
from core.engines.decision_engine import DecisionEngine


def test_analyze_compare():
    engine = DecisionEngine()

    result = engine.analyze(
        "bandingkan kuliah atau kerja"
    )

    assert result == DecisionIntent.COMPARE


def test_analyze_decide():
    engine = DecisionEngine()

    result = engine.analyze(
        "bantu aku memilih laptop A atau laptop B"
    )

    assert result == DecisionIntent.DECIDE


def test_analyze_unknown():
    engine = DecisionEngine()

    result = engine.analyze(
        "ingat bahwa aku suka kopi"
    )

    assert result == DecisionIntent.UNKNOWN


def test_extract_options():
    engine = DecisionEngine()

    options = engine.extract_options(
        "bandingkan kuliah atau kerja"
    )

    assert options == ["kuliah", "kerja"]


def test_extract_options_unknown():
    engine = DecisionEngine()

    options = engine.extract_options(
        "halo AURA"
    )

    assert options == []


def test_validate_options():
    engine = DecisionEngine()

    assert engine.validate_options(
        ["kuliah", "kerja"]
    )


def test_validate_invalid_options():
    engine = DecisionEngine()

    assert not engine.validate_options(
        ["kuliah"]
    )


def test_compare_options():
    engine = DecisionEngine()

    result = engine.compare_options(
        ["kuliah", "kerja"]
    )

    assert "kuliah" in result
    assert "kerja" in result


def test_make_decision():
    engine = DecisionEngine()

    result = engine.make_decision(
        ["kuliah", "kerja"]
    )

    assert "kuliah" in result


def test_process_compare():
    engine = DecisionEngine()

    result = engine.process(
        "bandingkan kuliah atau kerja"
    )

    assert result is not None
    assert "kuliah" in result
    assert "kerja" in result


def test_process_decide():
    engine = DecisionEngine()

    result = engine.process(
        "bantu aku memilih kuliah atau kerja"
    )

    assert result is not None
    assert "kuliah" in result


def test_process_invalid_options():
    engine = DecisionEngine()

    result = engine.process(
        "bandingkan kuliah"
    )

    assert result is not None
    assert "setidaknya dua pilihan" in result


def test_process_unknown():
    engine = DecisionEngine()

    result = engine.process(
        "halo AURA"
    )

    assert result is None