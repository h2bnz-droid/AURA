from core.context import AuraContext
from core.memory_retrieval import MemoryRetrieval

from services.profile_service import owner_name
from services.conversation_service import history
from services.emotion_service import latest_emotion
from services.temporal_service import event_history
from services.reflection_service import latest
from services.relationship_service import get_all_relationships
from services.cognitive_model_service import get_all
from services.long_term_context_service import collect_long_term_context
from services.integrated_cognitive_context_service import (
    IntegratedCognitiveContextService,
)
from services.adaptive_personalization_service import (
    AdaptivePersonalizationService,
)

memory_retrieval = MemoryRetrieval()
integrated_cognitive_context_service = (
    IntegratedCognitiveContextService()
)
adaptive_personalization_service = (
    AdaptivePersonalizationService()
)

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

    #Recent reflections
    context.reflections = latest()

    #Relationship
    context.relationships = get_all_relationships()

    # Personal cognitive Model
    context.cognitive_model = get_all()

    long_term_context = collect_long_term_context()

    context.long_term_context = [
        _normalize_long_term_context_item(item)
        for item in long_term_context
    ]

    context.integrated_cognitive_context = (
        build_integrated_cognitive_context(user_input)
    )

    context.personalization = (
        adaptive_personalization_service.build_context()
    )

    return context

def _normalize_long_term_context_item(item):
    if isinstance(item, dict):
        return item

    return {
        "content": item.content,
        "category": item.category,
        "source": item.source,
        "confidence": item.confidence,
        "relevance": item.relevance,
        "created_at": item.created_at,
        "updated_at": item.updated_at,
    }

def build_integrated_cognitive_context(user_input: str):
    return integrated_cognitive_context_service.build()