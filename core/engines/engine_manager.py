from core.engines.profile_engine import ProfileEngine
from core.engines.memory_engine import MemoryEngine
from core.engines.goal_engine import GoalEngine
from core.engines.planner_engine import PlannerEngine
from core.engines.decision_engine import DecisionEngine
from core.engines.knowledge_engine import KnowledgeEngine
from core.engines.learning_engine import LearningEngine
from core.engines.emotion_engine import EmotionEngine
from core.engines.temporal_engine import TemporalEngine
from core.engines.reflection_engine import ReflectionEngine
from core.engines.relationship_engine import RelationshipEngine
from core.engines.mindset_engine import MindsetEngine
from core.engines.conversation_engine import ConversationEngine


class EngineManager:

    def __init__(self):
        self.engines = [
            ProfileEngine(),
            MemoryEngine(),
            GoalEngine(),
            PlannerEngine(),
            DecisionEngine(),
            KnowledgeEngine(),
            LearningEngine(),
            EmotionEngine(),
            TemporalEngine(),
            ReflectionEngine(),
            RelationshipEngine(),
            MindsetEngine(),
            ConversationEngine(),
        ]

    def process(
        self,
        message: str,
        context=None,
    ) -> str | None:

        for engine in self.engines:

            # Engine yang sudah mendukung context
            if (
                context is not None
                and hasattr(engine, "process_with_context")
            ):
                response = engine.process_with_context(
                    message,
                    context,
                )

            # Engine lama tetap menggunakan kontrak lama
            else:
                response = engine.process(message)

            if response:
                return response

        return None
