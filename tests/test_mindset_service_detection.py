from services.mindset_service import detect_mindset


def test_detect_growth_mindset():
    result = detect_mindset(
        "Aku ingin meningkatkan kemampuan Python"
    )

    assert result is not None
    assert result.name == "growth"


def test_detect_resilient_mindset():
    result = detect_mindset(
        "Aku gagal lagi dan rasanya ingin menyerah"
    )

    assert result is not None
    assert result.name == "resilient"


def test_detect_reflective_mindset():
    result = detect_mindset(
        "Aku ingin evaluasi dari pengalaman ini"
    )

    assert result is not None
    assert result.name == "reflective"


def test_detect_mindset_unknown():
    assert detect_mindset("halo AURA") is None

def test_detect_mindset_prioritizes_resilient_over_growth():
    result = detect_mindset(
        "Aku gagal belajar lagi dan ingin menyerah"
    )

    assert result is not None
    assert result.name == "resilient"