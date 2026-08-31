from core.domain.relationship_intent import RelationshipIntent
from core.engines.relationship_engine import RelationshipEngine


def test_relationship_engine_analyze_create():
    engine = RelationshipEngine()

    result = engine.analyze(
        "Aku punya teman bernama Budi"
    )

    assert result == RelationshipIntent.CREATE


def test_relationship_engine_analyze_show():
    engine = RelationshipEngine()

    result = engine.analyze(
        "lihat relasi"
    )

    assert result == RelationshipIntent.SHOW


def test_relationship_engine_analyze_update():
    engine = RelationshipEngine()

    result = engine.analyze(
        "ubah relasi Budi menjadi colleague"
    )

    assert result == RelationshipIntent.UPDATE


def test_relationship_engine_analyze_unknown():
    engine = RelationshipEngine()

    result = engine.analyze(
        "Halo AURA"
    )

    assert result == RelationshipIntent.UNKNOWN_INTENT


def test_relationship_engine_parse_create():
    engine = RelationshipEngine()

    result = engine._parse_create(
        "Aku punya teman bernama Budi"
    )

    assert result == ("Budi", "teman")


def test_relationship_engine_parse_create_invalid():
    engine = RelationshipEngine()

    result = engine._parse_create(
        "Aku punya teman"
    )

    assert result is None


def test_relationship_engine_parse_update():
    engine = RelationshipEngine()

    result = engine._parse_update(
        "ubah relasi Budi menjadi colleague"
    )

    assert result == ("Budi", "colleague")


def test_relationship_engine_parse_update_invalid():
    engine = RelationshipEngine()

    result = engine._parse_update(
        "ubah relasi Budi"
    )

    assert result is None


def test_relationship_engine_create_invalid_format():
    engine = RelationshipEngine()

    result = engine.process(
        "Aku punya teman"
    )

    assert result is not None
    assert "Format relationship belum dikenali" in result


def test_relationship_engine_update_missing_relationship():
    engine = RelationshipEngine()

    result = engine.process(
        "ubah relasi TidakAda menjadi colleague"
    )

    assert result is not None
    assert "belum ditemukan" in result