import re

from core.domain.goal_intent import GoalIntent
from services.goal_service import active_goals, add_goal, abandon, find_active_goal, finish_goal, set_progress
from core.engines.base_engine import BaseEngine

class GoalEngine(BaseEngine):
    """Mengelola tujuan pengguna dengan perintah Bahasa Indonesia sederhana."""

    CREATE_PREFIXES = ("aku ingin ", "saya ingin ", "ingin ", "mau ", "bertekad ", "target ", "cita-cita ", "goal ")
    SHOW_PATTERNS = ("goal saya", "goals saya", "goalku", "target saya", "tujuan saya", "lihat goal")
    UPDATE_PREFIXES = ("update goal ", "progres goal ", "kemajuan goal ")
    COMPLETE_PREFIXES = ("selesaikan goal ", "selesai goal ", "tuntaskan goal ", "goal selesai ")
    ABANDON_PREFIXES = ("batalkan goal ", "berhenti goal ", "tinggalkan goal ")

    def analyze(self, message: str) -> GoalIntent:
        text = message.strip().casefold()
        if any(pattern in text for pattern in self.SHOW_PATTERNS):
            return GoalIntent.SHOW
        if any(text.startswith(prefix) for prefix in self.COMPLETE_PREFIXES):
            return GoalIntent.COMPLETE
        if any(text.startswith(prefix) for prefix in self.ABANDON_PREFIXES):
            return GoalIntent.ABANDON
        if self._parse_progress(text):
            return GoalIntent.UPDATE
        if any(text.startswith(prefix) for prefix in self.CREATE_PREFIXES):
            return GoalIntent.CREATE
        return GoalIntent.UNKNOWN

    @staticmethod
    def _strip_prefix(text: str, prefixes: tuple[str, ...]) -> str:
        lowered = text.casefold()
        for prefix in prefixes:
            if lowered.startswith(prefix):
                return text[len(prefix):].strip(" .")
        return text.strip(" .")

    def extract_goal(self, message: str) -> str:
        return self._strip_prefix(message.strip(), self.CREATE_PREFIXES)

    @staticmethod
    def _parse_progress(message: str):
        match = re.match(r"(?:update|progres|kemajuan)\\s+(?:goal\\s+)?(.+?)\\s+(?:menjadi\\s+)?(\\d{1,3})%?$", message.strip(), re.IGNORECASE)
        if not match:
            return None
        title, progress = match.groups()
        value = int(progress)
        return (title.strip(" ."), value) if 0 <= value <= 100 else None

    def validate_goal(self, title: str) -> bool:
        if not title or len(title.strip()) < 3:
            return False
        return True

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent == GoalIntent.CREATE:
            title = self.extract_goal(message)
            if not self.validate_goal(title):
                return "Ceritakan tujuanmu sedikit lebih jelas agar bisa aku catat."
            add_goal(title)
            return f'Baik, aku sudah menambahkan tujuan "{title}". Langkah kecil pertama apa yang realistis kamu lakukan hari ini?'

        if intent == GoalIntent.SHOW:
            goals = active_goals()
            if not goals:
                return "Saat ini kamu belum memiliki tujuan aktif. Ceritakan satu hal yang ingin kamu capai."
            return "\\n".join(["Tujuan aktifmu:"] + [f"{index}. {goal['title']} — {goal['progress']}%" for index, goal in enumerate(goals, 1)])

        if intent == GoalIntent.UPDATE:
            title, progress = self._parse_progress(message)
            goal = find_active_goal(title)
            if not goal:
                return f'Aku tidak menemukan tujuan aktif "{title}". Ketik "goal saya" untuk melihat daftarnya.'
            set_progress(goal["id"], progress)
            if progress == 100:
                finish_goal(goal["id"])
                return f'Hebat, tujuan "{goal["title"]}" sudah selesai! Luangkan sejenak untuk merayakan kemajuanmu.'
            return f'Progress "{goal["title"]}" sudah diperbarui menjadi {progress}%. Apa langkah kecil berikutnya?'

        if intent in (GoalIntent.COMPLETE, GoalIntent.ABANDON):
            prefixes = self.COMPLETE_PREFIXES if intent == GoalIntent.COMPLETE else self.ABANDON_PREFIXES
            title = self._strip_prefix(message, prefixes)
            goal = find_active_goal(title)
            if not goal:
                return f'Aku tidak menemukan tujuan aktif "{title}". Ketik "goal saya" untuk melihat daftarnya.'
            if intent == GoalIntent.COMPLETE:
                finish_goal(goal["id"])
                return f'Selamat, tujuan "{goal["title"]}" sudah ditandai selesai.'
            abandon(goal["id"])
            return f'Tujuan "{goal["title"]}" sudah dihentikan. Tidak apa-apa mengubah arah saat kondisimu berubah.'

        return None

    def get_goals(self):
        return active_goals()