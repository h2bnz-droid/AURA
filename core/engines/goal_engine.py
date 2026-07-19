from core.models.goal import Goal


class GoalEngine:

    def add(self, goal: Goal):
        pass

    def update(self, goal: Goal):
        pass

    def complete(self, goal_id: int):
        pass

    def delete(self, goal_id: int):
        pass

    def active(self):
        return []

    def completed(self):
        return []