from core.engines.base_engine import BaseEngine
from core.domain.decision_intent import DecisionIntent


class DecisionEngine(BaseEngine):

    COMPARE_PREFIXES = (
        "bandingkan ",
        "coba bandingkan ",
        "apa perbedaan ",
        "mana yang lebih baik ",
    )

    DECIDE_PREFIXES = (
        "bantu aku memilih ",
        "bantu saya memilih ",
        "bantu pilih ",
        "pilihkan ",
        "mana yang harus aku pilih ",
        "mana yang sebaiknya aku pilih ",
    )

    def __init__(self):
        super().__init__()

    def analyze(self, message: str) -> DecisionIntent:
        text = message.strip().casefold()

        if any(
            text.startswith(prefix)
            for prefix in self.COMPARE_PREFIXES
        ):
            return DecisionIntent.COMPARE

        if any(
            text.startswith(prefix)
            for prefix in self.DECIDE_PREFIXES
        ):
            return DecisionIntent.DECIDE

        return DecisionIntent.UNKNOWN

    def extract_options(
        self,
        message: str,
    ) -> list[str]:

        text = message.strip()

        for prefix in (
            *self.COMPARE_PREFIXES,
            *self.DECIDE_PREFIXES,
        ):
            if text.casefold().startswith(prefix):
                content = text[len(prefix):].strip(" .")
                return [
                    option.strip()
                    for option in content.split(" atau ")
                    if option.strip()
                ]

        return []

    def validate_options(
        self,
        options: list[str],
    ) -> bool:

        return len(options) >= 2

    def compare_options(
        self,
        options: list[str],
    ) -> str:

        return (
            "Berikut pilihan yang bisa dibandingkan:\n"
            + "\n".join(
                f"{index}. {option}"
                for index, option in enumerate(options, 1)
            )
        )

    def make_decision(
        self,
        options: list[str],
    ) -> str:

        return (
            f"Berdasarkan pilihan yang diberikan, "
            f"aku menyarankan mempertimbangkan "
            f'"{options[0]}" terlebih dahulu.'
        )

    def process(self, message: str) -> str | None:

        intent = self.analyze(message)

        if intent == DecisionIntent.UNKNOWN:
            return None

        options = self.extract_options(message)

        if not self.validate_options(options):
            return (
                "Aku membutuhkan setidaknya dua pilihan "
                "agar bisa membantumu mengambil keputusan."
            )

        if intent == DecisionIntent.COMPARE:
            return self.compare_options(options)

        if intent == DecisionIntent.DECIDE:
            return self.make_decision(options)

        return None