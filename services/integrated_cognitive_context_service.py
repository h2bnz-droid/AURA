from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
    IntegratedCognitiveContext,
)


class IntegratedCognitiveContextService:

    def build(
        self,
        stable=None,
        relevant=None,
        recent=None,
    ) -> IntegratedCognitiveContext:

        return IntegratedCognitiveContext(
            stable=self._normalize(stable),
            relevant=self._normalize(relevant),
            recent=self._normalize(recent),
        )

    def _normalize(self, items):
        if not items:
            return []

        normalized = []
        seen = set()

        for item in items:
            if isinstance(item, CognitiveContextItem):
                context_item = item
            else:
                context_item = CognitiveContextItem(
                    category=str(item.get("category", "")).strip().casefold(),
                    value=item.get("value"),
                    source=str(item.get("source", "")).strip(),
                    confidence=float(item.get("confidence", 0.0)),
                    relevance=float(item.get("relevance", 0.0)),
                )

            key = (
                context_item.category,
                str(context_item.value).strip().casefold(),
            )

            if key in seen:
                continue

            seen.add(key)
            normalized.append(context_item)

        return normalized