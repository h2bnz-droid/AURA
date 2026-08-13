from core.context import AuraContext
from core.memory_retrieval import MemoryRetrieval

from services.profile_service import owner_name
from services.conversation_service import history


memory_retrieval = MemoryRetrieval()


def build_context(user_input: str) -> AuraContext:
    context = AuraContext(user_input)

    # Profile
    context.profile = owner_name()

    # Relevant memories
    context.memories = memory_retrieval.retrieve(user_input)

    # Recent conversation
    context.history = history(6)

    return context