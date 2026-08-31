from core.domain.emotion_intent import EmotionIntent
from core.engines.base_engine import BaseEngine
from services.emotion_service import record_emotion


class EmotionEngine(BaseEngine):

    EMOTION_KEYWORDS = {
        "happy": (
            "senang",
            "bahagia",
            "gembira",
            "lega",
        ),
        "sad": (
            "sedih",
            "kecewa",
            "menangis",
            "hampa",
        ),
        "angry": (
            "marah",
            "kesal",
            "jengkel",
            "emosi",
        ),
        "frustrated": (
            "frustrasi",
            "susah",
            "sulit",
            "bingung",
        ),
        "anxious": (
            "cemas",
            "khawatir",
            "takut",
            "gelisah",
        ),
        "excited": (
            "semangat",
            "antusias",
            "excited",
            "tidak sabar",
        ),
        "tired": (
            "capek",
            "lelah",
            "letih",
            "kelelahan",
        ),
    }

    def analyze(self, message: str) -> EmotionIntent:
        text = message.strip().casefold()

        if "apa emosiku" in text:
            return EmotionIntent.SHOW

        if "emosiku" in text or "perasaanku" in text:
            return EmotionIntent.TRACK

        if self.detect_emotion(text):
            return EmotionIntent.DETECT

        return EmotionIntent.UNKNOWN

    def detect_emotion(self, message: str) -> str | None:
        text = message.strip().casefold()

        for emotion, keywords in self.EMOTION_KEYWORDS.items():
            if any(keyword in text for keyword in keywords):
                return emotion

        return None

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == EmotionIntent.DETECT:
            emotion = self.detect_emotion(message)

            if emotion is None:
                return None

            record_emotion(
                emotion,
                0.5,
                "user_message",
            )

            return f"Aku menangkap bahwa kamu sedang merasa {emotion}."

        if intent == EmotionIntent.SHOW:
            return "Aku akan menampilkan emosimu."

        if intent == EmotionIntent.TRACK:
            return "Aku akan melacak perkembangan emosimu."

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
                "Aku menangkap",
                "Saya menangkap",
            ).replace(
                "Aku akan menampilkan",
                "Saya akan menampilkan",
            ).replace(
                "Aku akan melacak",
                "Saya akan melacak",
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