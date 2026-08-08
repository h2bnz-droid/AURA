from core.engines.base_engine import BaseEngine
from core.domain.conversation_intent import ConversationIntent


class ConversationEngine(BaseEngine):

    GREETING_PREFIXES = (
        "halo",
        "hai",
        "hi",
        "hey",
        "selamat pagi",
        "selamat siang",
        "selamat sore",
        "selamat malam",
    )

    def __init__(self):
        super().__init__()

    def analyze(self, message: str) -> ConversationIntent:
        text = message.strip().casefold()

        if any(
            text.startswith(prefix)
            for prefix in self.GREETING_PREFIXES
        ):
            return ConversationIntent.GREETING

        if text:
            return ConversationIntent.CHAT

        return ConversationIntent.UNKNOWN

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == ConversationIntent.GREETING:
            return "Halo! Ada yang bisa aku bantu?"

        if intent == ConversationIntent.CHAT:
            return "Aku siap mendengarkan. Ceritakan saja apa yang ingin kamu bicarakan."

        return None