from services.memory_service import remember


def execute(text):

    lower = text.lower()

    if not lower.startswith("ingatkan"):
        return None

    reminder = text[8:].strip()

    if not reminder:
        return "Apa yang ingin saya ingatkan?"

    remember(
        "reminder",
        "task",
        reminder
    )

    return f"Baik, saya menyimpan pengingat: {reminder}"