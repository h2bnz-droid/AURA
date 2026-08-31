from services.mindset_service import detect_mindset


def test_detect_growth_mindset():
    result = detect_mindset("Aku ingin belajar Python lagi.")

    assert result is not None
    assert result.name == "growth"


def test_detect_resilient_mindset():
    result = detect_mindset("Aku mengalami kesulitan dan ingin bangkit.")

    assert result is not None
    assert result.name == "resilient"


def test_detect_reflective_mindset():
    result = detect_mindset("Aku ingin evaluasi pengalaman ini.")

    assert result is not None
    assert result.name == "reflective"


def test_detect_mindset_returns_none_when_unknown():
    assert detect_mindset("Halo AURA") is None