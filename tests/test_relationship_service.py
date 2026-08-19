from services.relationship_service import (
    normalize_relationship_type,
    save_relationship,
    get_relationship,
    get_all_relationships,
    update_relationship,
)


def test_relationship_service():
    assert normalize_relationship_type(" FRIEND ") == "friend"
    assert normalize_relationship_type("unknown-type") == "other"

    save_relationship(
        "Siti",
        "Mother",
        "active",
        "Ibu pengguna",
    )

    relationship = get_relationship("Siti")

    assert relationship is not None
    assert relationship["person_name"] == "Siti"
    assert relationship["relationship_type"] == "mother"

    update_relationship(
        "Siti",
        "family",
        "active",
        "Keluarga",
    )

    relationship = get_relationship("Siti")

    assert relationship["relationship_type"] == "family"
    assert relationship["note"] == "Keluarga"

    relationships = get_all_relationships()

    assert len(relationships) >= 1