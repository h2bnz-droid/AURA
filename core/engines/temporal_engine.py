import re

from core.domain.temporal_intent import TemporalIntent
from core.engines.base_engine import BaseEngine

from services.temporal_service import (
    event_history,
    latest_event,
    calculate_trend,
)


class TemporalEngine(BaseEngine):

    def analyze(self, message: str) -> TemporalIntent:
        text = message.strip().casefold()

        if any(
            phrase in text
            for phrase in (
                "trend",
                "perkembangan",
                "perubahan",
                "meningkat",
                "menurun",
            )
        ):
            return TemporalIntent.TREND

        if any(
            phrase in text
            for phrase in (
                "riwayat",
                "history",
                "sebelumnya",
                "belakangan ini",
            )
        ):
            return TemporalIntent.HISTORY

        if any(
            phrase in text
            for phrase in (
                "kondisi saya",
                "keadaan saya",
                "state saya",
                "kondisiku",
            )
        ):
            return TemporalIntent.STATE

        return TemporalIntent.UNKNOWN

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == TemporalIntent.TREND:
            return self._process_trend(message)

        if intent == TemporalIntent.HISTORY:
            return self._process_history(message)

        if intent == TemporalIntent.STATE:
            return self._process_state()

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
                "Aku belum tahu",
                "Saya belum mengetahui",
            ).replace(
                "Belum cukup data",
                "Data yang tersedia belum cukup",
            ).replace(
                "Belum ada riwayat",
                "Belum terdapat riwayat",
            ).replace(
                "Belum ada data",
                "Belum terdapat data",
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

    def _extract_subject(self, message: str) -> str | None:
        text = message.strip()

        match = re.search(
            r"(?:trend|perkembangan|perubahan|riwayat|history)\s+(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return None

    def _process_trend(self, message: str) -> str:
        subject = self._extract_subject(message)

        if not subject:
            return "Aku belum tahu apa yang ingin kamu lihat perkembangannya."

        history = event_history(
            subject=subject,
        )

        values = []

        for event in history:
            value = event.get("value")

            try:
                values.append(float(value))
            except (TypeError, ValueError):
                continue

        if len(values) < 2:
            return f"Belum cukup data untuk melihat trend {subject}."

        trend = calculate_trend(values)

        if trend == "increasing":
            return f"Trend {subject} sedang meningkat."

        if trend == "decreasing":
            return f"Trend {subject} sedang menurun."

        return f"Trend {subject} relatif stabil."

    def _process_history(self, message: str) -> str:
        subject = self._extract_subject(message)

        if not subject:
            return "Aku belum tahu riwayat apa yang ingin kamu lihat."

        history = event_history(
            subject=subject,
        )

        if not history:
            return f"Belum ada riwayat untuk {subject}."

        return "\n".join(
            f"- {event['value']}"
            for event in history
        )

    def _process_state(self) -> str:
        emotion = latest_event(
            "emotion",
            "current",
        )

        if emotion is None:
            return "Belum ada data kondisi terkini."

        return (
            f"Kondisi terakhir yang tercatat: "
            f"{emotion['value']}."
        )