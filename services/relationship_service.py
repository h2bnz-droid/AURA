from datetime import datetime

from database.relationships import (
    save_relationship as db_save_relationship,
    get_relationship as db_get_relationship,
    get_all_relationships as db_get_all_relationships,
    update_relationship as db_update_relationship,
)


RELATIONSHIP_TYPE_MAP = {
    "friend": "friend",
    "teman": "friend",

    "family": "family",
    "keluarga": "family",

    "mother": "mother",
    "ibu": "mother",

    "father": "father",
    "ayah": "father",

    "sibling": "sibling",
    "saudara": "sibling",
    "kakak": "sibling",
    "adik": "sibling",

    "partner": "partner",
    "pasangan": "partner",

    "colleague": "colleague",
    "rekan kerja": "colleague",

    "other": "other",
}


def normalize_relationship_type(value: str) -> str:
    relationship_type = value.strip().casefold()

    return RELATIONSHIP_TYPE_MAP.get(
        relationship_type,
        "other",
    )


def save_relationship(
    person_name: str,
    relationship_type: str,
    status: str | None = None,
    note: str | None = None,
) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db_save_relationship(
        person_name.strip(),
        normalize_relationship_type(relationship_type),
        status.strip() if status else None,
        note.strip() if note else None,
        now,
        now,
    )


def get_relationship(person_name: str):
    return db_get_relationship(person_name.strip())


def get_all_relationships():
    return db_get_all_relationships()


def update_relationship(
    person_name: str,
    relationship_type: str,
    status: str | None = None,
    note: str | None = None,
) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    db_update_relationship(
        person_name.strip(),
        normalize_relationship_type(relationship_type),
        status.strip() if status else None,
        note.strip() if note else None,
        now,
    )