from core.domain.context_priority import ContextPriority


class ContextPrioritizationService:

    DEFAULT_LIMIT = 10

    DEFAULT_PRIORITIES = {
        "mindset": 1.0,
        "active_mindset": 1.0,
        "cognitive_state": 1.0,
        "cognitive_behavior": 0.95,
        "emotion": 0.9,
        "memory": 0.85,
        "personalization": 0.8,
        "long_term_context": 0.7,
        "relationship": 0.65,
        "reflection": 0.6,
        "temporal": 0.55,
        "history": 0.5,
    }

    def prioritize(self, items, limit=None):
        prioritized = self.prioritize_all(items)

        if limit is None:
            limit = self.DEFAULT_LIMIT

        return prioritized[:limit]

    def prioritize_all(self, items):
        prioritized = [
            self._to_context_priority(item)
            for item in items
        ]

        prioritized = self._remove_duplicates(prioritized)

        prioritized.sort(
            key=lambda item: item.priority,
            reverse=True,
        )

        return prioritized

    def _to_context_priority(self, item):
        priority = self.DEFAULT_PRIORITIES.get(
            item.category,
            0.0,
        )

        return ContextPriority(
            category=item.category,
            value=item.value,
            priority=priority,
            source=getattr(item, "source", None),
            confidence=getattr(item, "confidence", None),
            relevance=getattr(item, "relevance", None),
        )

    def _remove_duplicates(self, items):
        unique_items = []
        seen = set()

        for item in items:
            key = (
                item.category.lower(),
                str(item.value).lower(),
            )

            if key in seen:
                continue

            seen.add(key)
            unique_items.append(item)

        return unique_items