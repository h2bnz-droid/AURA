from core.router import process_user_input


class AuraKernel:
    """Kernel utama AURA."""

    def process(self, message: str) -> str:
        self.before_process(message)

        response = process_user_input(message)

        self.after_process(message, response)

        return response

    def before_process(self, message: str):
        pass

    def after_process(self, message: str, response: str):
        pass