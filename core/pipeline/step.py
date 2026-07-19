from abc import ABC, abstractmethod

from core.context import AuraContext


class PipelineStep(ABC):
    """
    Base class untuk seluruh pipeline AURA.
    """

    @abstractmethod
    def execute(self, context: AuraContext):
        pass