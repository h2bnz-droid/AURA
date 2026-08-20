from services.cognitive_model_service import (
    save,
    get,
    get_all,
    update,
    delete,
)


def test_save_and_get_cognitive_attribute():
    save(
        attribute_name="interest",
        attribute_value="robotics",
        category="interest",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    attribute = get("interest")

    assert attribute is not None
    assert attribute["attribute_value"] == "robotics"


def test_get_all_cognitive_attributes():
    attributes = get_all()

    assert attributes is not None


def test_update_cognitive_attribute():
    update(
        attribute_name="interest",
        attribute_value="robotics and AI",
        category="interest",
        source="user_statement",
        confidence=1.0,
        updated_at="2026-08-20T01:00:00",
    )

    attribute = get("interest")

    assert attribute is not None
    assert attribute["attribute_value"] == "robotics and AI"


def test_delete_cognitive_attribute():
    delete("interest")

    attribute = get("interest")

    assert attribute is None