from abc import ABC, abstractmethod

class BaseEngine(ABC):

    @abstractmethod
    def analyze(self, message: str):
        """Analyze the message and determine the intent."""
        pass

    @abstractmethod
    def process(self, message: str):
        """Process the message based on the determined intent."""
        pass