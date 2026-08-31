from core.domain.mindset import Mindset
from core.engines.base_engine import BaseEngine
from services.mindset_service import find_mindset, get_mindsets


class MindsetEngine(BaseEngine):

    SHOW_PREFIXES = (
        "lihat mindset",
        "tampilkan mindset",
        "lihat pola pikir",
        "tampilkan pola pikir",
    )

    FIND_PREFIXES = (
        "jelaskan mindset ",
        "jelaskan pola pikir ",
        "apa itu mindset ",
        "apa itu pola pikir ",
    )

    def analyze(self, message: str) -> str | None:
        text = message.strip().casefold()

        for prefix in self.SHOW_PREFIXES:
            if text.startswith(prefix):
                return "show"

        for prefix in self.FIND_PREFIXES:
            if text.startswith(prefix):
                return "find"

        return None

    def _extract_name(self, message: str) -> str:
        text = message.strip()

        for prefix in self.FIND_PREFIXES:
            if text.casefold().startswith(prefix):
                return text[len(prefix):].strip()

        return ""

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == "show":
            mindsets = get_mindsets()

            return "\n".join(
                f"- {mindset.name}: {mindset.description}"
                for mindset in mindsets
            )

        if intent == "find":
            name = self._extract_name(message)
            mindset = find_mindset(name)

            if mindset is None:
                return f"Mindset '{name}' belum dikenali."

            return (
                f"{mindset.name}: "
                f"{mindset.description}"
            )

        return None

    def process_with_context(self, message: str, context) -> str | None:
        intent = self.analyze(message)

        if intent == "find":
            name = self._extract_name(message)
            mindset = find_mindset(name)

            if mindset is not None:
                context.active_mindset = mindset

        result = self.process(message)

        if result:
            return result

        return None