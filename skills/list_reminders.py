from services.memory_service import reminders


def execute(text):

    lower = text.lower()

    if "pengingat" not in lower:
        return None

    data = reminders()

    if not data:
        return "Belum ada pengingat."

    result = ["Daftar pengingat:"]

    for item in data:
        result.append(
            f"- {item['memory_value']}"
        )

    return "\n".join(result)