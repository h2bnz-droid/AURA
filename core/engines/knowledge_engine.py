from core.engines.base_engine import BaseEngine
from core.domain.knowledge_intent import KnowledgeIntent


class KnowledgeEngine(BaseEngine):

    SEARCH_PREFIXES = (
        "cari tahu ",
        "carikan informasi ",
        "cari informasi ",
        "apa informasi tentang ",
    )

    EXPLAIN_PREFIXES = (
        "jelaskan ",
        "terangkan ",
        "apa itu ",
        "jelaskan tentang ",
    )

    def __init__(self):
        super().__init__()

    def analyze(self, message: str) -> KnowledgeIntent:
        text = message.strip().casefold()

        if any(
            text.startswith(prefix)
            for prefix in self.SEARCH_PREFIXES
        ):
            return KnowledgeIntent.SEARCH

        if any(
            text.startswith(prefix)
            for prefix in self.EXPLAIN_PREFIXES
        ):
            return KnowledgeIntent.EXPLAIN

        return KnowledgeIntent.UNKNOWN

    def extract_query(self, message: str) -> str | None:
        text = message.strip()
        lower = text.casefold()

        for prefix in (
            *self.SEARCH_PREFIXES,
            *self.EXPLAIN_PREFIXES,
        ):
            if lower.startswith(prefix):
                query = text[len(prefix):].strip(" .")

                if query.casefold().startswith("tentang "):
                    query = query[8:].strip()

                return query

        return None

    def validate_query(self, query: str | None) -> bool:
        if not query or len(query.strip()) < 3:
            return False

        return True

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == KnowledgeIntent.UNKNOWN:
            return None

        query = self.extract_query(message)

        if not self.validate_query(query):
            return (
                "Aku membutuhkan topik atau pertanyaan "
                "yang lebih jelas."
            )

        return (
            f"Aku akan membantu mencari informasi "
            f"tentang: {query}"
        )