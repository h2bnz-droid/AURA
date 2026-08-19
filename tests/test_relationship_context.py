from core.context_builder import build_context


def test_context_builder_includes_relationships():
    from services.relationship_service import save_relationship

    save_relationship(
        "Budi",
        "friend",
        "active",
        "Teman",
    )

    context = build_context(
        "lihat relasi"
    )

    assert context.relationships
    assert context.relationships[0]["person_name"] == "Budi"