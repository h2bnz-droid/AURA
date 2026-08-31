from core.domain.reflection_intent import ReflectionIntent
from core.engines.base_engine import BaseEngine

from services.profile_service import get_profile
from services.memory_service import recall_all
from services.goal_service import active_goals
from services.reflection_service import latest, save

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
        profile = context["profile"]
        memory = context["memory"]
        goals = context["goals"]

        user_name = profile["name"] if profile else "Kamu"

        if not goals:
            return {
                "summary": (
                    f"{user_name}, kamu belum memiliki tujuan yang tercatat. "
                    "Cobalah menetapkan tujuan terlebih dahulu agar refleksi "
                    "bisa lebih terarah."
                ),
                "insights": (
                    "Belum ada tujuan yang cukup untuk dianalisis."
                ),
                "questions": (
                    "Apa tujuan yang ingin kamu capai saat ini?"
                ),
            }

        if not memory:
            return {
                "summary": (
                    f"{user_name}, kamu memiliki tujuan yang tercatat, "
                    "tetapi belum ada catatan pengalaman yang tersimpan."
                ),
                "insights": (
                    "Catatan pengalaman akan membantu menghubungkan tujuan "
                    "dengan perkembanganmu."
                ),
                "questions": (
                    "Pengalaman apa yang paling berpengaruh terhadap tujuanmu?"
                ),
            }

        return {
            "summary": (
                f"{user_name}, berdasarkan catatan pengalaman dan tujuanmu, "
                "berikut refleksi awal yang bisa kamu pertimbangkan."
            ),
            "insights": (
                "Pengalaman yang tersimpan dapat digunakan untuk melihat "
                "hubungan antara pengalaman dan tujuan."
            ),
            "questions": (
                "Apa yang sudah berjalan baik, dan apa yang ingin kamu perbaiki?"
            ),
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
