class AuraKernel:
    """Core orchestrator untuk seluruh request AURA."""

    def process(self, message: str) -> str:
        raise NotImplementedError