from core.context import AuraContext
from core.memory_retrieval import MemoryRetrieval
from core.domain.integrated_cognitive_context import (
    CognitiveContextItem,
)
from core.cognitive_behavior import CognitiveBehavior

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
from services.mindset_service import (
    get_mindsets,
    detect_mindset,
)
from services.cognitive_state_service import CognitiveStateService
from services.cognitive_state_evolution_service import (
    CognitiveStateEvolutionService,
)

memory_retrieval = MemoryRetrieval()
integrated_cognitive_context_service = (
    IntegratedCognitiveContextService()
)
adaptive_personalization_service = (
    AdaptivePersonalizationService()
)
cognitive_state_service = CognitiveStateService()
cognitive_state_evolution_service = (
    CognitiveStateEvolutionService()
)
cognitive_behavior = CognitiveBehavior()

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

    context.personalization = (
        adaptive_personalization_service.build_context()
    )

    # Mindsets
    context.mindsets = get_mindsets()
    context.active_mindset = detect_mindset(user_input)

    # Cognitive State
    context.cognitive_state = cognitive_state_service.latest()

    # Cognitive State History
    context.cognitive_state_history = (
        cognitive_state_service.history_context()
    )

    # Cognitive State Evolution
    context.cognitive_state_evolution = (
        cognitive_state_evolution_service.analyze(
            cognitive_state=context.cognitive_state,
            cognitive_state_history=context.cognitive_state_history,
        )
    )

    # Cognitive Behavior
    context.cognitive_behavior = cognitive_behavior.build(
        context.cognitive_state
    )

    # Integrated Cognitive Context
    context.integrated_cognitive_context = (
        build_integrated_cognitive_context(user_input)
    )

    _add_cognitive_state_to_context(
        context.integrated_cognitive_context,
        context.cognitive_state,
    )

    _add_cognitive_state_history_to_context(
        context.integrated_cognitive_context,
        context.cognitive_state_history,
    )

    _add_cognitive_state_evolution_to_context(
        context.integrated_cognitive_context,
        context.cognitive_state_evolution,
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

def build_integrated_cognitive_context(
    user_input: str,
    cognitive_state=None,
):
    mindsets = get_mindsets()

    mindset_items = [
        {
            "category": "mindset",
            "value": mindset.name,
            "source": "mindset_service",
            "confidence": 1.0,
            "relevance": 0.0,
        }
        for mindset in mindsets
    ]

    recent_items = []

    if cognitive_state is not None:

        if cognitive_state.mindset is not None:
            recent_items.append(
                {
                    "category": "mindset",
                    "value": cognitive_state.mindset,
                    "source": cognitive_state.source,
                    "confidence": 1.0,
                    "relevance": 1.0,
                }
            )

        if cognitive_state.emotion is not None:
            recent_items.append(
                {
                    "category": "emotion",
                    "value": cognitive_state.emotion,
                    "source": cognitive_state.source,
                    "confidence": 1.0,
                    "relevance": 1.0,
                }
            )

    return integrated_cognitive_context_service.build(
        relevant=mindset_items,
        recent=recent_items,
    )

def _add_cognitive_state_to_context(
    integrated_context,
    cognitive_state,
):
    if cognitive_state is None:
        return

    if cognitive_state.mindset:
        integrated_context.recent.append(
            CognitiveContextItem(
                category="mindset",
                value=cognitive_state.mindset,
                source=cognitive_state.source,
                confidence=1.0,
                relevance=1.0,
            )
        )

    if cognitive_state.emotion:
        integrated_context.recent.append(
            CognitiveContextItem(
                category="emotion",
                value=cognitive_state.emotion,
                source=cognitive_state.source,
                confidence=1.0,
                relevance=1.0,
            )
        )

def _add_cognitive_state_history_to_context(
    integrated_context,
    cognitive_state_history,
):
    if cognitive_state_history is None:
        return

    for history_item in cognitive_state_history.items:
        integrated_context.recent.append(
            CognitiveContextItem(
                category=f"{history_item.state_type}_history",
                value=history_item.value,
                source=history_item.source,
                confidence=history_item.confidence,
                relevance=0.5,
            )
        )

def _add_cognitive_state_evolution_to_context(
    integrated_context,
    cognitive_state_evolution,
):
    if cognitive_state_evolution is None:
        return

    for evolution in cognitive_state_evolution:
        if evolution.status == "unknown":
            continue

        integrated_context.recent.append(
            CognitiveContextItem(
                category=f"{evolution.state_type}_evolution",
                value=evolution.status,
                source="cognitive_state_evolution",
                confidence=1.0,
                relevance=0.6,
            )
        )