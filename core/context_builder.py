from core.context import AuraContext

from services.profile_service import owner_name
from services.memory_service import search
from services.conversation_service import history


def build_context(user_input: str):

    context = AuraContext(user_input)

    # Profile
    context.profile = owner_name()

    # Memory
    words = user_input.lower().split()

    found = []

    for word in words:
        found.extend(search(word))

    # Hilangkan duplikasi
    seen = set()

    unique = []

    for memory in found:

        value = memory["memory_value"]

        if value not in seen:
            seen.add(value)
            unique.append(memory)

    context.memories = unique

    # History
    context.history = history(6)

    return context