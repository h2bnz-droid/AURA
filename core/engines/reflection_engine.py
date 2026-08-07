from enum import Enum, auto
from services.profile_service import get_profile
from services.memory_service import recall_all
from services.goal_service import active_goals
from services.reflection_service import latest
from services.reflection_service import save
from services.reflection_service import name
from core.engines.base_engine import BaseEngine

class ReflectionIntent(Enum):
    """Mengelola refleksi pengguna dengan perintah Bahasa Indonesia sederhana."""

    REFLECT = auto()
    SHOW_REFLECTIONS = auto()
    UNKNOWN_INTENT = auto()

class ReflectionEngine(BaseEngine):
    REFLECT_PREFIXES = ("aku ingin merenung", "aku ingin refleksi", "mau refleksi", "mau merenung")
    SHOW_REFLECTIONS_PATTERNS = ("lihat refleksi", "tampilkan refleksi", "refleksi saya", "refleksi terakhir")  
    UNKNOWN_INTENT = ReflectionIntent.UNKNOWN_INTENT

    def analyze(self, message: str) -> ReflectionIntent:
        text = message.strip().casefold()

        for prefix in self.REFLECT_PREFIXES:
            if text.startswith(prefix):
                return ReflectionIntent.REFLECT

        for pattern in self.SHOW_REFLECTIONS_PATTERNS:
            if pattern in text:
                return ReflectionIntent.SHOW_REFLECTIONS

        return self.UNKNOWN_INTENT

    def collect_context(self) -> dict:
        profile = get_profile()

        if profile:
            name = profile["name"]

        memory = recall_all()
        goals = active_goals()
        return {
            "profile": profile,
            "memory": memory,
            "goals": goals
        }

    def generate_reflection(self, context: dict) -> dict[str, str]:
        memory = context["memory"]
        goals = context["goals"]

        if not goals:
            return {
                
                "summary": f"{name}, Kamu belum memiliki tujuan yang tercatat. Cobalah untuk menetapkan tujuan terlebih dahulu agar aku bisa membantumu merenung.",
                "insights": "Beberapa wawasan yang bisa diambil dari pengalamanmu",
                "questions": "Pertanyaan reflektif untuk membantu kamu merenung lebih dalam"
            }

        if goals and not memory:
            return {
                "summary": f"{name}, Kamu memiliki tujuan yang tercatat, tetapi belum ada catatan pengalaman yang tersimpan. Cobalah untuk mencatat pengalamanmu terlebih dahulu agar aku bisa membantumu merenung.",
                "insights": "Beberapa wawasan yang bisa diambil dari pengalamanmu",
                "questions": "Pertanyaan reflektif untuk membantu kamu merenung lebih dalam"
            }

        return {
            "summary": f"{name}, Berdasarkan catatan pengalaman dan tujuanmu, berikut adalah refleksi yang bisa aku berikan: ...",
            "insights": "Beberapa wawasan yang bisa diambil dari pengalaman dan tujuanmu",
            "questions": "Pertanyaan reflektif untuk membantu kamu merenung lebih dalam"
        }

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == ReflectionIntent.REFLECT:
            context = self.collect_context()
            if not context["memory"] and not context["goals"]:
                return "Ceritakan sedikit tentang pengalamanmu agar aku bisa membantumu merenung."
            reflection = self.generate_reflection(context)

            save(
                reflection["summary"],
                reflection["insights"],
                reflection["questions"]

            )

            return (
                f"Refleksi berdasarkan catatan pengalaman dan tujuanmu:\n\n"
                f"{reflection['summary']}\n\n"
                f"Wawasan: {reflection['insights']}\n\n"
                f"Pertanyaan reflektif: {reflection['questions']}"
            )

        elif intent == ReflectionIntent.SHOW_REFLECTIONS:
            reflections = self.latest_reflections()
            if not reflections:
                return "Belum ada refleksi yang tersimpan."
            return "\n".join(
                item["summary"] for item in reflections
            )

        return None

    def latest_reflections(self):
        return latest()
