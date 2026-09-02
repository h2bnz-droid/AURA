class CognitiveBehavior:

    def build(self, cognitive_state):

        if not cognitive_state:
            return None

        instructions = []

        mindset = cognitive_state.mindset
        emotion = cognitive_state.emotion

        if emotion == "anxious":
            instructions.append(
                "Gunakan nada yang menenangkan dan membantu "
                "pengguna merasa lebih aman."
            )

        elif emotion == "sad":
            instructions.append(
                "Tunjukkan empati dan hindari respons yang "
                "terlalu keras atau menghakimi."
            )

        elif emotion == "happy":
            instructions.append(
                "Gunakan respons yang positif dan mendukung."
            )

        if mindset == "resilient":
            instructions.append(
                "Dorong pengguna untuk melihat kesulitan sebagai "
                "sesuatu yang dapat dihadapi secara bertahap."
            )

        elif mindset == "growth":
            instructions.append(
                "Dorong proses belajar dan perkembangan "
                "daripada hanya fokus pada hasil."
            )

        elif mindset == "reflective":
            instructions.append(
                "Ajak pengguna untuk mempertimbangkan pengalaman "
                "dan mengambil pelajaran dari situasi."
            )

        if not instructions:
            return None

        return " ".join(instructions)