class AuraContext:
    def __init__(self, user_input: str):
        self.user_input = user_input

        self.profile = None
        self.memories = []
        self.history = []
        self.emotion = None
        self.temporal = []
        self.reflections = []
        self.relationships = []
        self.cognitive_model = ()
        self.mindsets = []
        self.active_mindset = None
        self.long_term_context = []
        self.integrated_cognitive_context = None
        self.personalization = None

        self.response = None