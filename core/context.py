class AuraContext:
    def __init__(self, user_input: str):
        self.user_input = user_input

        self.profile = None
        self.memories = []
        self.history = []
        self.emotion = None
        self.temporal = []
        self.reflections = []

        self.response = None