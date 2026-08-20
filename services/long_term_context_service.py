from core.domain.long_term_context import LongTermContext
from services.profile_service import owner_name
from services.memory_service import recall_all
from services.goal_service import active_goals
from services.reflection_service import latest
from services.relationship_service import get_all_relationships
from services.learning_service import active_learning
from services.cognitive_model_service import get_all

def normalize_content(content: str) -> str:
    return " ".join(content.strip().split())


def normalize_category(category: str) -> str:
    return category.strip().casefold()


def create_context(
    content: str,
    category: str,
    source: str,
    confidence: float,
    relevance: float,
    created_at: str,
    updated_at: str,
) -> LongTermContext:
    return LongTermContext(
        content=normalize_content(content),
        category=normalize_category(category),
        source=source.strip(),
        confidence=confidence,
        relevance=relevance,
        created_at=created_at,
        updated_at=updated_at,
    )


def deduplicate_context(
    contexts: list[LongTermContext],
) -> list[LongTermContext]:
    unique = []
    seen = set()

    for context in contexts:
        key = (
            context.content.casefold(),
            context.category,
            context.source,
        )

        if key in seen:
            continue

        seen.add(key)
        unique.append(context)

    return unique


def filter_by_relevance(
    contexts: list[LongTermContext],
    minimum_relevance: float = 0.0,
) -> list[LongTermContext]:
    return [
        context
        for context in contexts
        if context.relevance >= minimum_relevance
    ]


def get_stable_context(
    contexts: list[LongTermContext],
) -> list[LongTermContext]:
    stable_categories = {
        "identity",
        "preference",
        "value",
        "interest",
        "skill",
        "habit",
        "aspiration",
        "life_stage",
    }

    return [
        context
        for context in contexts
        if context.category in stable_categories
    ]


def get_relevant_context(
    contexts: list[LongTermContext],
    minimum_relevance: float = 0.5,
) -> list[LongTermContext]:
    return filter_by_relevance(
        contexts,
        minimum_relevance,
    )


def get_recent_context(
    contexts: list[LongTermContext],
) -> list[LongTermContext]:
    return sorted(
        contexts,
        key=lambda context: context.updated_at,
        reverse=True,
    )


def aggregate_context(
    contexts: list[LongTermContext],
) -> list[LongTermContext]:
    normalized = [
        create_context(
            content=context.content,
            category=context.category,
            source=context.source,
            confidence=context.confidence,
            relevance=context.relevance,
            created_at=context.created_at,
            updated_at=context.updated_at,
        )
        for context in contexts
    ]

    return deduplicate_context(normalized)

def collect_long_term_context() -> list[LongTermContext]:
    contexts = []

    # Profile
    name = owner_name()

    if name:
        contexts.append(
            create_context(
                content=name,
                category="identity",
                source="profile",
                confidence=1.0,
                relevance=1.0,
                created_at="",
                updated_at="",
            )
        )

    # Memory
    memories = recall_all()

    if isinstance(memories, list):
        for memory in memories:
            if not isinstance(memory, dict):
                continue

            value = memory.get("memory_value")

            if not value:
                continue

            contexts.append(
                create_context(
                    content=value,
                    category=memory.get("category", "memory"),
                    source="memory",
                    confidence=1.0,
                    relevance=0.8,
                    created_at="",
                    updated_at="",
                )
            )

    # Goals
    for goal in active_goals():
        contexts.append(
            create_context(
                content=_get_value(goal, "title", 1),
                category="goal",
                source="goal",
                confidence=1.0,
                relevance=0.9,
                created_at=_get_value(goal, "created_at", 7),
                updated_at=_get_value(goal, "updated_at", 8),
            )
        )

    # Reflections
    for reflection in latest():
        contexts.append(
            create_context(
                content=_get_value(reflection, "summary", 1),
                category="reflection",
                source="reflection",
                confidence=1.0,
                relevance=0.7,
                created_at=_get_value(reflection, "created_at", 4),
                updated_at=_get_value(reflection, "created_at", 4),
            )
        )

    # Relationships
    for relationship in get_all_relationships():
        contexts.append(
            create_context(
                content=_get_value(relationship, "person_name", 1),
                category="relationship",
                source="relationship",
                confidence=1.0,
                relevance=0.8,
                created_at=_get_value(relationship, "created_at", 5),
                updated_at=_get_value(relationship, "updated_at", 6),
            )
        )

    # Learning
    for learning in active_learning():
        contexts.append(
            create_context(
                content=learning["topic"],
                category="learning",
                source="learning",
                confidence=1.0,
                relevance=0.8,
                created_at=learning["created_at"],
                updated_at=learning["updated_at"],
            )
        )

    # Personal Cognitive Model
    for attribute in get_all():
        contexts.append(
            create_context(
                content=_get_value(attribute, "attribute_value", 2),
                category=_get_value(attribute, "category", 3),
                source=_get_value(attribute, "source", 4),
                confidence=_get_value(attribute, "confidence", 5),
                relevance=0.9,
                created_at=_get_value(attribute, "created_at", 6),
                updated_at=_get_value(attribute, "updated_at", 7),
            )
        )

    return aggregate_context(contexts)

def _get_value(row, key: str, index: int):
    if isinstance(row, dict):
        return row.get(key)

    try:
        return row[key]
    except (IndexError, KeyError, TypeError):
        return row[index]