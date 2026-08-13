import re

from services.memory_service import search


class MemoryRetrieval:

    MAX_RESULTS = 5

    def _normalize_word(self, word: str) -> str:
        return re.sub(r"[^\w]", "", word.lower())

    def score(self, user_input: str, memory: dict) -> int:
        input_words = {
            self._normalize_word(word)
            for word in user_input.split()
        }

        memory_words = {
            self._normalize_word(word)
            for word in memory["memory_value"].split()
        }

        input_words.discard("")
        memory_words.discard("")

        return len(input_words & memory_words)

    def retrieve(self, user_input: str) -> list:
        words = {
            self._normalize_word(word)
            for word in user_input.split()
        }

        words.discard("")

        found = []

        for word in words:
            found.extend(search(word))

        seen = set()
        unique = []

        for memory in found:
            value = memory["memory_value"]

            if value not in seen:
                seen.add(value)
                unique.append(memory)

        ranked = sorted(
            unique,
            key=lambda memory: self.score(user_input, memory),
            reverse=True,
        )

        ranked = [
            memory
            for memory in ranked
            if self.score(user_input, memory) > 0
        ]

        return ranked[:self.MAX_RESULTS]