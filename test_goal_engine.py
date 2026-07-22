from core.engines.goal_engine import GoalEngine

engine = GoalEngine()

examples = [
    "Aku ingin menjadi Cyber Security Engineer.",
    "Hari ini aku belajar Python.",
    "Alhamdulillah aku lulus sertifikasi.",
    "Aku batal ikut lomba.",
    "Apa goal-ku sekarang?"
]

for text in examples:
    intent = engine.analyze(text)
    print(f"{text}")
    print(f"-> {intent.name}\n")