import re

from core.domain.learning_intent import LearningIntent
from core.engines.base_engine import BaseEngine
from services.learning_service import (
    start_learning,
    active_learning,
    update_learning_progress,
)


class LearningEngine(BaseEngine):

    def analyze(self, message: str) -> LearningIntent:
        text = message.strip().casefold()

        if "sedang belajar" in text:
            return LearningIntent.START

        if text.startswith("progress ") and "%" in text:
            return LearningIntent.PROGRESS

        if "apa yang sedang kupelajari" in text:
            return LearningIntent.SHOW

        return LearningIntent.UNKNOWN

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == LearningIntent.START:
            topic = self._extract_topic(message)

            if not topic:
                return None

            start_learning(topic)

            return "Aku akan mencatat proses belajarmu."

        if intent == LearningIntent.PROGRESS:
            topic, progress = self._extract_progress(message)

            if not topic:
                return None

            update_learning_progress(topic, progress)

            return "Aku akan mencatat progress belajarmu."

        if intent == LearningIntent.SHOW:
            learning = active_learning()

            if not learning:
                return "Belum ada pembelajaran aktif."

            lines = ["Pembelajaran aktif:"]

            for index, item in enumerate(learning, 1):
                lines.append(
                    f"{index}. {item['topic']} — {item['progress']}%"
                )

            return "\n".join(lines)

        return None

    def process_with_context(
        self,
        message: str,
        context,
    ) -> str | None:
        result = self.process(message)

        if result is None:
            return None

        response_style = self._get_response_style(context)

        if response_style == "formal":
            return result.replace(
                "Aku akan mencatat",
                "Saya akan mencatat",
            )

        return result

    def _get_response_style(self, context) -> str:
        if not context:
            return "default"

        if isinstance(context, dict):
            personalization = context.get(
                "personalization",
                context,
            )
        else:
            personalization = getattr(
                context,
                "personalization",
                None,
            )

        if not personalization:
            return "default"

        return personalization.get(
            "response_style",
            "default",
        )

    @staticmethod
    def _extract_topic(message: str) -> str:
        text = message.strip()

        marker = "sedang belajar"
        index = text.casefold().find(marker)

        if index == -1:
            return ""

        return text[index + len(marker):].strip()

    @staticmethod
    def _extract_progress(message: str) -> tuple[str, int]:
        match = re.match(
            r"progress\s+(.+?)\s+(\d{1,3})%",
            message.strip(),
            re.IGNORECASE,
        )

        if not match:
            return "", 0

        topic = match.group(1).strip()
        progress = int(match.group(2))

        if not 0 <= progress <= 100:
            return "", 0

        return topic, progress