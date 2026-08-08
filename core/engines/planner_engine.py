from core.engines.base_engine import BaseEngine
from core.domain.planner_intent import PlannerIntent
from services.planner_service import save_plan

class PlannerEngine(BaseEngine):

    CREATE_PLAN_PREFIXES = (
        "buat rencana untuk ",
        "rencanakan ",
        "buat rencana ",
        "rencana untuk ",
        "susun rencana",
        "buat roadmap",
        "buat strategi",
    )

    def __init__(self):
        super().__init__()

    def analyze(self, message: str) -> PlannerIntent:
        text = message.strip().casefold()

        if any(
            text.startswith(prefix) 
            for prefix in self.CREATE_PLAN_PREFIXES
        ):
            return PlannerIntent.CREATE_PLAN

        return PlannerIntent.UNKNOWN

    def extract_goal(self, message: str) -> str | None:
        text = message.strip()
        lower = text.casefold()

        for prefix in self.CREATE_PLAN_PREFIXES:
            if lower.startswith(prefix):
                return text[len(prefix):].strip(" .")
        return None

    def validate_goal(self, goal: str | None) -> bool:
        # Implement your goal validation logic here
        if not goal or len(goal.strip()) < 3:
            return False

        return True

    def generate_plan(self, goal: str) -> list[str]:
        # Implement your plan generation logic here
        return [
            "Langkah pertama",
            "Langkah kedua",
            "Langkah ketiga",
        ]

    def process(self, message: str) -> str | None:
        intent = self.analyze(message)

        if intent != PlannerIntent.CREATE_PLAN:
            return None
        
        goal = self.extract_goal(message)

        if not self.validate_goal(goal):
            return (
                "Tujuan yang diberikan tidak valid."
                " Silakan berikan tujuan yang lebih jelas."
            )

        plan = self.generate_plan(goal)

        save_plan(goal, plan)

        steps = "\n".join(
            f"{index}. {step}" 
            for index, step in enumerate(plan,1)
            )

        return (
            f'Baik, aku telah membuat rencana untuk tujuan "{goal}":\n\n'
            f"{steps}"
        )
