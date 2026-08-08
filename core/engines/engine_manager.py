from core.engines.profile_engine import ProfileEngine
from core.engines.memory_engine import MemoryEngine
from core.engines.goal_engine import GoalEngine
from core.engines.planner_engine import PlannerEngine
from core.engines.decision_engine import DecisionEngine
from core.engines.knowledge_engine import KnowledgeEngine
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
            ConversationEngine(),
        ]

    def process(self, message: str) -> str | None:
        for engine in self.engines:
            response = engine.process(message)

            if response:
                return response

        return None