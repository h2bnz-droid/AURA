from core.engines.profile_engine import ProfileEngine
from core.engines.memory_engine import MemoryEngine
from core.engines.goal_engine import GoalEngine


class EngineManager:

    def __init__(self):
        self.engines = [
            ProfileEngine(),
            MemoryEngine(),
            GoalEngine(),
        ]

    def process(self, message: str):

        for engine in self.engines:

            response = engine.process(message)

            if response:
                return response

        return None