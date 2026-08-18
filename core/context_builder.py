from core.context import AuraContext
from core.memory_retrieval import MemoryRetrieval

from services.profile_service import owner_name
from services.conversation_service import history
from services.emotion_service import latest_emotion
from services.temporal_service import event_history

memory_retrieval = MemoryRetrieval()


def build_context(user_input: str) -> AuraContext:
    context = AuraContext(user_input)

    # Profile
    context.profile = owner_name()

    # Relevant memories
    context.memories = memory_retrieval.retrieve(user_input)

    # Recent conversation
    context.history = history(6)

    #Temporal events
    context.temporal = event_history()

    # Current emotion
    context.emotion = latest_emotion()

    return context