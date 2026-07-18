from services.memory_service import search
from services.profile_service import owner_name
from services.conversation_service import history


def build_context(user_input: str):

    context = []

    name = owner_name()

    if name:
        context.append(f"Nama pengguna: {name}")

    # Cari memori relevan
    words = user_input.lower().split()

    found = []

    for word in words:
        found.extend(search(word))

    if found:
        context.append("")
        context.append("Memori yang relevan:")

        # Hilangkan duplikasi
        seen = set()

        for memory in found:

            value = memory["memory_value"]

            if value not in seen:
                seen.add(value)
                context.append(f"- {value}")

    # Riwayat percakapan
    chats = history(6)

    if chats:
        context.append("")
        context.append("Percakapan terakhir:")

        for chat in chats:
            context.append(
                f"{chat['role']}: {chat['message']}"
            )

    context.append("")
    context.append(f"Pertanyaan pengguna: {user_input}")

    return "\n".join(context)