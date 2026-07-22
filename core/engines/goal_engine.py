from core.domain.goal_intent import GoalIntent
from services.goal_service import (
    add_goal,
    active_goals
)

class GoalEngine:
    """Engine untuk menganalisis dan mengelola tujuan pengguna."""

    def analyze(self, message: str) -> GoalIntent:
        """Mendeteksi intent terkait goal dari pesan pengguna."""

        text = message.lower()

        #Menampilkan goal
        if any(word in text for word in [
            "goal saya",
            "target saya",
            "tujuan saya",
            "apa goal",
            "goals saya",
            "goals-ku",
            "goalku"
        ]):
            return GoalIntent.SHOW

        # Membuat goal baru
        if any(word in text for word in [
            "ingin",
            "mau",
            "bertekad",
            "target",
            "cita-cita",
        ]):
            return GoalIntent.CREATE

        # Update progress
        if any(word in text for word in [
            "sedang",
            "progres",
            "kemajuan",
            "lanjut",
            "update"
        ]):
            return GoalIntent.UPDATE

        # Goal selesai
        if any(word in text for word in [
            "selesai",
            "berhasil",
            "lulus",
            "tercapai"
        ]):
            return GoalIntent.COMPLETE

        # Goal dibatalkan
        if any(word in text for word in [
            "batal",
            "berhenti",
            "menyerah"
        ]):
            return GoalIntent.ABANDON

        return GoalIntent.UNKNOWN
    
    def extract_title(self, message: str) -> str:
        """Mengekstrak judul goal dari pesan pengguna."""
        # Implementasi sederhana untuk mengekstak judul goal dari pesan. 
        # Bisa dilakukan dengan mencari kata-kata yang menunjukkan tujuan atau goal.
        # Contoh implementasi sederhana:
        text = message.strip()

        prefixes = [
            "aku ingin",
            "saya ingin",
            "ingin",
            "mau",
            "bertekad",
            "target",
            "cita-cita",
            "goal"
        ]
        
        lower = text.lower()
        for prefix in prefixes:
            if lower.startswith(prefix):
                return text[len(prefix):].strip()
        return text
    
    def process(self, message: str) -> str | None:

        intent = self.analyze(message)

        if intent == GoalIntent.CREATE:

            title = self.extract_title(message)
            DEFAULT_DESCRIPTION = "Deskripsi goal belum ditentukan."
            DEFAULT_CATEGORY = "General"
            DEFAULT_PRIORITY = 1
            target_date = None  # Bisa diubah sesuai kebutuhan

            add_goal(
                title,
                DEFAULT_DESCRIPTION,
                DEFAULT_CATEGORY,
                DEFAULT_PRIORITY,
                target_date
            )
            return f'Baik, aku sudah menambahkan goal "{title}".'
        
        if intent == GoalIntent.SHOW:

            goals = active_goals()
            
            if not goals:
                return "Saat ini kamu belum memiliki goal aktif."
            
            lines = ["Berikut adalah goal aktifmu:"]

            for i, goal in enumerate(goals, start=1):
                lines.append(f"{i}. {goal['title']} - Progress: {goal['progress']}%"
                )
            return "\n".join(lines)

    def normalize_title(title: str) -> str:
        return " ".join(word.capitalize() for word in title.split())
        
        return None