from core.engines.relationship_engine import RelationshipEngine
from services.relationship_service import get_relationship


def test_relationship_engine_uses_service_data():
    engine = RelationshipEngine()

    engine.process(
        "Aku punya teman bernama Andi"
    )

    relationship = get_relationship("Andi")

    assert relationship is not None
    assert relationship["person_name"] == "Andi"
    assert relationship["relationship_type"] == "friend"

def test_relationship_update_persists_through_service():
    engine = RelationshipEngine()

    engine.process(
        "Aku punya teman bernama Budi"
    )

    engine.process(
        "ubah relasi Budi menjadi colleague"
    )

    relationship = get_relationship("Budi")

    assert relationship is not None
    assert relationship["relationship_type"] == "colleague"