from core.router import process


class AuraKernel:
    """Kernel utama AURA."""

    def process(self, message: str) -> str:
        self.before_process(message)

        response = process(message)

        self.after_process(message, response)

        return response

    def before_process(self, message: str):
        """Hook sebelum request diproses."""
        pass

    def after_process(self, message: str, response: str):
        """Hook setelah response dibuat."""
        pass