from database.relationships import (
    create_table,
    save_relationship,
    get_relationship,
    get_all_relationships,
    update_relationship,
)


def test_relationship_database_crud():
    create_table()

    save_relationship(
        "Budi",
        "friend",
        "active",
        "Teman sekolah",
        "2026-01-01 10:00:00",
        "2026-01-01 10:00:00",
    )

    relationship = get_relationship("Budi")

    assert relationship is not None
    assert relationship["person_name"] == "Budi"
    assert relationship["relationship_type"] == "friend"

    update_relationship(
        "Budi",
        "colleague",
        "active",
        "Teman kerja",
        "2026-01-02 10:00:00",
    )

    relationship = get_relationship("Budi")

    assert relationship["relationship_type"] == "colleague"
    assert relationship["note"] == "Teman kerja"

    relationships = get_all_relationships()

    assert len(relationships) >= 1