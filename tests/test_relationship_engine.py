from core.engines.relationship_engine import RelationshipEngine


def test_relationship_engine_create():
    engine = RelationshipEngine()

    response = engine.process(
        "Aku punya teman bernama Budi"
    )

    assert response is not None
    assert "Budi" in response


def test_relationship_engine_show():
    engine = RelationshipEngine()

    engine.process(
        "Aku punya teman bernama Budi"
    )

    response = engine.process("lihat relasi")

    assert response is not None
    assert "Budi" in response


def test_relationship_engine_update():
    engine = RelationshipEngine()

    engine.process(
        "Aku punya teman bernama Budi"
    )

    response = engine.process(
        "ubah relasi Budi menjadi colleague"
    )

    assert response is not None
    assert "colleague" in response


def test_relationship_engine_unknown():
    engine = RelationshipEngine()

    assert engine.process(
        "hari ini cuacanya bagus"
    ) is None