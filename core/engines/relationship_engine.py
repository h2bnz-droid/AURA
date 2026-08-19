from core.domain.relationship_intent import RelationshipIntent
from core.engines.base_engine import BaseEngine

from services.relationship_service import (
    save_relationship,
    get_relationship,
    get_all_relationships,
    update_relationship,
)


class RelationshipEngine(BaseEngine):

    UNKNOWN_INTENT = RelationshipIntent.UNKNOWN_INTENT

    SHOW_PATTERNS = (
        "tampilkan relasi",
        "lihat relasi",
        "tampilkan hubungan",
        "lihat hubungan",
        "relasi saya",
        "hubungan saya",
    )

    CREATE_PREFIXES = (
        "aku punya ",
        "saya punya ",
    )

    UPDATE_PREFIXES = (
        "ubah relasi ",
        "ubah hubungan ",
    )

    def analyze(self, message: str) -> RelationshipIntent:
        text = message.strip().casefold()

        for pattern in self.SHOW_PATTERNS:
            if pattern in text:
                return RelationshipIntent.SHOW

        for prefix in self.UPDATE_PREFIXES:
            if text.startswith(prefix):
                return RelationshipIntent.UPDATE

        for prefix in self.CREATE_PREFIXES:
            if text.startswith(prefix):
                return RelationshipIntent.CREATE

        return self.UNKNOWN_INTENT

    def _parse_create(self, message: str):
        text = message.strip()

        lower = text.casefold()

        for prefix in self.CREATE_PREFIXES:
            if lower.startswith(prefix):
                content = text[len(prefix):].strip()

                parts = content.split(" bernama ", 1)

                if len(parts) != 2:
                    return None

                relationship_type = parts[0].strip()
                person_name = parts[1].strip()

                if not relationship_type or not person_name:
                    return None

                return person_name, relationship_type

        return None

    def _parse_update(self, message: str):
        text = message.strip()

        lower = text.casefold()

        for prefix in self.UPDATE_PREFIXES:
            if lower.startswith(prefix):
                content = text[len(prefix):].strip()

                parts = content.split(" menjadi ", 1)

                if len(parts) != 2:
                    return None

                person_name = parts[0].strip()
                relationship_type = parts[1].strip()

                if not person_name or not relationship_type:
                    return None

                return person_name, relationship_type

        return None

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == RelationshipIntent.CREATE:
            parsed = self._parse_create(message)

            if not parsed:
                return (
                    "Format relationship belum dikenali. "
                    "Contoh: Aku punya teman bernama Budi."
                )

            person_name, relationship_type = parsed

            save_relationship(
                person_name,
                relationship_type,
            )

            return (
                f"Relationship dengan {person_name} "
                f"sebagai {relationship_type} berhasil disimpan."
            )

        if intent == RelationshipIntent.SHOW:
            relationships = get_all_relationships()

            if not relationships:
                return "Belum ada relationship yang tersimpan."

            return "\n".join(
                f"- {item['person_name']}: "
                f"{item['relationship_type']}"
                for item in relationships
            )

        if intent == RelationshipIntent.UPDATE:
            parsed = self._parse_update(message)

            if not parsed:
                return (
                    "Format update relationship belum dikenali. "
                    "Contoh: Ubah relasi Budi menjadi colleague."
                )

            person_name, relationship_type = parsed

            existing = get_relationship(person_name)

            if not existing:
                return (
                    f"Relationship dengan {person_name} "
                    "belum ditemukan."
                )

            update_relationship(
                person_name,
                relationship_type,
            )

            return (
                f"Relationship dengan {person_name} "
                f"berhasil diperbarui menjadi {relationship_type}."
            )

        return None