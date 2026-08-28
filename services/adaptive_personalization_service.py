from core.domain.personalization import (
    PersonalizationPreference,
    PersonalizationSignal,
)


class AdaptivePersonalizationService:
    def __init__(self) -> None:
        self._preferences: list[PersonalizationPreference] = []
        self._signals: list[PersonalizationSignal] = []

    def save_preference(
        self,
        preference: PersonalizationPreference,
    ) -> PersonalizationPreference:
        self._preferences.append(preference)
        return preference

    def get_preferences(self) -> list[PersonalizationPreference]:
        return list(self._preferences)

    def add_signal(
        self,
        signal: PersonalizationSignal,
    ) -> PersonalizationSignal:
        self._signals.append(signal)
        return signal

    def get_signals(self) -> list[PersonalizationSignal]:
        return list(self._signals)

    def get_high_confidence_signals(
        self,
        minimum_confidence: float = 0.8,
    ) -> list[PersonalizationSignal]:
        return sorted(
            (
                signal
                for signal in self._signals
                if signal.confidence >= minimum_confidence
            ),
            key=lambda signal: signal.timestamp,
        )

    def build_context(self) -> dict[str, str]:
        context = {
            preference.name: preference.value
            for preference in self._preferences
        }

        signals = self.get_high_confidence_signals()

        latest_signals = {}

        for signal in signals:
            latest_signals[signal.name] = signal.value

        for name, value in latest_signals.items():
            if name not in context:
                context[name] = value

        return context