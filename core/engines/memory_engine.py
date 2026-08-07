from core.domain.memory_intent import MemoryIntent
from core.engines.base_engine import BaseEngine
from services.memory_service import remember, search


class MemoryEngine(BaseEngine):
    def __init__(self):
        self.TRIGGERS = [
            "ingat bahwa",
            "ingat",
            "catat",
            "tolong ingat",
            "jangan lupa",
        ]

    def analyze(self, message: str) -> MemoryIntent:

        text = message.lower()

        triggers = [
            "ingat bahwa",
            "ingat",
            "catat",
            "tolong ingat",
            "jangan lupa",
        ]

        if any(text.startswith(trigger) for trigger in triggers):
            return MemoryIntent.REMEMBER

        return MemoryIntent.UNKNOWN

    def extract_memory(self, message: str) -> str | None:

        text = message.strip()
        lower = text.lower()

        for trigger in self.TRIGGERS:
            if lower.startswith(trigger):
                return text[len(trigger):].strip()

        return None

    def validate_memory(self, memory: str | None) -> bool:

        if not memory:
            return False

        if len(memory) < 2:
            return False
        
        return True 

    def process(self, message: str) -> str | None:

        intent = self.analyze(message)

        if intent != MemoryIntent.REMEMBER:
            return None

        memory = self.extract_memory(message)

        if not self.validate_memory(memory):
            return "apa yang harus aku ingat? Tolong beri tahu aku dengan jelas."

        remember(
            "note",
            "manual_note",
            memory
        )

        return f"Baik, aku akan mengingatnya: '{memory}'."

    def retrieve(self, message: str):

        keywords = set(message.lower().split())

        memories = []

        for word in keywords:
            memories.extend(search(word))

        return memories    
