from database.personal_cognitive_model import (
    save_attribute,
    get_attribute,
    get_all_attributes,
    update_attribute,
    delete_attribute,
)


def save(
    attribute_name: str,
    attribute_value: str,
    category: str,
    source: str,
    confidence: float,
    created_at: str,
    updated_at: str,
):
    save_attribute(
        attribute_name=attribute_name,
        attribute_value=attribute_value,
        category=category,
        source=source,
        confidence=confidence,
        created_at=created_at,
        updated_at=updated_at,
    )


def get(attribute_name: str):
    return get_attribute(attribute_name)


def get_all():
    return get_all_attributes()


def update(
    attribute_name: str,
    attribute_value: str,
    category: str,
    source: str,
    confidence: float,
    updated_at: str,
):
    update_attribute(
        attribute_name=attribute_name,
        attribute_value=attribute_value,
        category=category,
        source=source,
        confidence=confidence,
        updated_at=updated_at,
    )


def delete(attribute_name: str):
    delete_attribute(attribute_name)