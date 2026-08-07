from core.engines.base_engine import BaseEngine
from core.domain.profile_intent import ProfileIntent
from services.profile_service import (
    create_profile,
    change_name,
    owner_name
)

class ProfileEngine(BaseEngine):

    def analyze(self, message: str) -> ProfileIntent:

        text = message.lower()

        if text.startswith("namaku ") or text.startswith("nama saya "):
            return ProfileIntent.SET_NAME

        return ProfileIntent.UNKNOWN

    def extract_name(self, message: str) -> str | None:

        text = message.strip()
        lower = text.lower()

        if lower.startswith("namaku "):
            return text[7:].strip()

        if lower.startswith("nama saya "):
            return text[10:].strip()

        return None

    def validate_name(self, name: str) -> bool:
        
        if not name or len(name) < 2:
            return False

        invalid_names = {
            "siapa",
            "siapa?",
            "apa",
            "apa?",
            "aku",
            "kamu"
        }

        if name.lower() in invalid_names:
            return False

        return True

    def process(self, message: str) -> str | None:

        intent = self.analyze(message)

        if intent != ProfileIntent.SET_NAME:
            return None

        name = self.extract_name(message)

        if not self.validate_name(name):
            return "Maaf, aku tidak bisa mengingat nama itu. Bisa coba lagi?"

        current_name = owner_name()

        if current_name:
            change_name(name)
        else:
            create_profile(name)        

        return f"Baik, mulai sekarang aku akan memanggilmu {name}."

    def get_profile(self):

        return {
            "name": owner_name()
        }