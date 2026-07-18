class AuraContext:
    def __init__(self, user_input: str):
        self.user_input = user_input

        self.profile = None
        self.memories = []
        self.history = []

        self.response = None