from database.personal_cognitive_model import (
    create_table,
    save_attribute,
    get_attribute,
    get_all_attributes,
    update_attribute,
    delete_attribute,
)


def test_create_personal_cognitive_model_table():
    create_table()


def test_save_and_get_attribute():
    create_table()

    save_attribute(
        attribute_name="skill",
        attribute_value="Python",
        category="skill",
        source="user_statement",
        confidence=1.0,
        created_at="2026-08-20T00:00:00",
        updated_at="2026-08-20T00:00:00",
    )

    attribute = get_attribute("skill")

    assert attribute is not None
    assert attribute["attribute_name"] == "skill"
    assert attribute["attribute_value"] == "Python"
    assert attribute["confidence"] == 1.0


def test_update_attribute():
    create_table()

    update_attribute(
        attribute_name="skill",
        attribute_value="Python + SQL",
        category="skill",
        source="user_statement",
        confidence=1.0,
        updated_at="2026-08-20T01:00:00",
    )

    attribute = get_attribute("skill")

    assert attribute is not None
    assert attribute["attribute_value"] == "Python + SQL"


def test_get_all_attributes():
    create_table()

    attributes = get_all_attributes()

    assert attributes is not None


def test_delete_attribute():
    create_table()

    delete_attribute("skill")

    attribute = get_attribute("skill")

    assert attribute is None