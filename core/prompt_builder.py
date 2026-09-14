from core.context import AuraContext
from core.security import redact_sensitive_data
from services.context_prioritization_service import (
    ContextPrioritizationService,
)


class PromptBuilder:

    def __init__(self):
        self.context_prioritization_service = (
            ContextPrioritizationService()
        )

    @staticmethod
    def _safe(value) -> str:
        """
        Convert context values to string and redact sensitive data
        before entering the AI prompt.
        """

        if value is None:
            return ""

        return redact_sensitive_data(str(value))

    def build(self, context: AuraContext) -> str:

        prompt = []

        prompt.append("==============================")
        prompt.append("AURA INTERNAL CONTEXT")
        prompt.append("==============================")

        # Profile
        if context.profile:
            prompt.append("")
            prompt.append("[PROFILE]")
            prompt.append(
                f"Nama: {self._safe(context.profile)}"
            )

        # Memory
        if context.memories:
            prompt.append("")
            prompt.append("[MEMORY]")

            for memory in context.memories:
                prompt.append(
                    f"- {self._safe(memory['memory_value'])}"
                )

        # Emotion
        if context.emotion:
            prompt.append("")
            prompt.append("[EMOTION]")

            prompt.append(
                f"Emosi terakhir: "
                f"{self._safe(context.emotion['emotion'])}"
            )

            prompt.append(
                f"Intensitas: "
                f"{self._safe(context.emotion['intensity'])}"
            )

        # Temporal Context
        if context.temporal:
            prompt.append("")
            prompt.append("[TEMPORAL CONTEXT]")

            for event in context.temporal:
                prompt.append(
                    f"- {self._safe(event['event_type'])}: "
                    f"{self._safe(event['subject'])} = "
                    f"{self._safe(event['value'])}"
                )

        # Reflections
        if context.reflections:
            prompt.append("")
            prompt.append("[REFLECTION]")

            for reflection in context.reflections:
                prompt.append(
                    f"- {self._safe(reflection['summary'])}"
                )

        # Relationships
        if context.relationships:
            prompt.append("")
            prompt.append("[RELATIONSHIP]")

            for relationship in context.relationships:
                prompt.append(
                    f"- {self._safe(relationship['person_name'])}: "
                    f"{self._safe(relationship['relationship_type'])}"
                )

        # Personal Cognitive Model
        if context.cognitive_model:
            prompt.append("")
            prompt.append(
                "[PERSONAL COGNITIVE MODEL]"
            )

            for attribute in context.cognitive_model:
                prompt.append(
                    f"- {self._safe(attribute['attribute_name'])}: "
                    f"{self._safe(attribute['attribute_value'])}"
                )

        # Mindsets
        if context.mindsets:
            prompt.append("")
            prompt.append("[MINDSET]")

            for mindset in context.mindsets:
                prompt.append(
                    f"- {self._safe(mindset.name)}: "
                    f"{self._safe(mindset.description)}"
                )

        # Active Mindset
        if context.active_mindset:
            prompt.append("")
            prompt.append("[ACTIVE MINDSET]")

            prompt.append(
                f"- {self._safe(context.active_mindset.name)}: "
                f"{self._safe(context.active_mindset.description)}"
            )

        # Personalization
        if context.personalization:
            prompt.append("")
            prompt.append("[PERSONALIZATION]")

            for name, value in (
                context.personalization.items()
            ):
                prompt.append(
                    f"- {self._safe(name)}: "
                    f"{self._safe(value)}"
                )

        # Long-Term Context
        if context.long_term_context:
            prompt.append("")
            prompt.append("[LONG-TERM CONTEXT]")

            for item in context.long_term_context:
                prompt.append(
                    f"- {self._safe(item['content'])}"
                )

        # Cognitive State
        cognitive_state = getattr(
            context,
            "cognitive_state",
            None,
        )

        if cognitive_state:
            prompt.append("")
            prompt.append("[COGNITIVE STATE]")

            if cognitive_state.mindset:
                prompt.append(
                    f"- Mindset: "
                    f"{self._safe(cognitive_state.mindset)}"
                )

            if cognitive_state.emotion:
                prompt.append(
                    f"- Emotion: "
                    f"{self._safe(cognitive_state.emotion)}"
                )

            prompt.append(
                f"- Source: "
                f"{self._safe(cognitive_state.source)}"
            )

        # Cognitive State History
        cognitive_state_history = getattr(
            context,
            "cognitive_state_history",
            None,
        )

        if cognitive_state_history:
            items = cognitive_state_history.items

            if items:
                prompt.append("")
                prompt.append(
                    "[COGNITIVE STATE HISTORY]"
                )

                for item in items:
                    prompt.append(
                        f"- {self._safe(item.state_type)}: "
                        f"{self._safe(item.value)}"
                    )

        # Cognitive State Evolution
        cognitive_state_evolution = getattr(
            context,
            "cognitive_state_evolution",
            None,
        )

        valid_evolutions = [
            evolution
            for evolution in (
                cognitive_state_evolution or []
            )
            if evolution.status != "unknown"
        ]

        if valid_evolutions:
            prompt.append("")
            prompt.append(
                "[COGNITIVE STATE EVOLUTION]"
            )

            for evolution in valid_evolutions:
                prompt.append(
                    f"- {self._safe(evolution.state_type)}: "
                    f"{self._safe(evolution.status)}"
                )

        # Cognitive Behavior
        cognitive_behavior = getattr(
            context,
            "cognitive_behavior",
            None,
        )

        if cognitive_behavior:
            prompt.append("")
            prompt.append("[COGNITIVE BEHAVIOR]")
            prompt.append(
                self._safe(cognitive_behavior)
            )

        # Integrated Cognitive Context
        if context.integrated_cognitive_context:
            integrated_context = (
                context.integrated_cognitive_context
            )

            # Collect all cognitive context layers.
            #
            # Priority must be calculated globally instead
            # of independently for stable, relevant,
            # and recent layers.
            all_items = (
                integrated_context.all_items()
            )

            prioritized_items = (
                self.context_prioritization_service.prioritize(
                    all_items
                )
            )

            if prioritized_items:
                prompt.append("")
                prompt.append(
                    "[INTEGRATED COGNITIVE CONTEXT]"
                )

                for item in prioritized_items:
                    prompt.append(
                        f"- {self._safe(item.category)}: "
                        f"{self._safe(item.value)}"
                    )

        # Recent Conversation
        if context.history:
            prompt.append("")
            prompt.append("[RECENT CONVERSATION]")

            for chat in context.history:
                prompt.append(
                    f"{self._safe(chat['role'])}: "
                    f"{self._safe(chat['message'])}"
                )

        # Current User Message
        prompt.append("")
        prompt.append("==============================")
        prompt.append("CURRENT USER MESSAGE")
        prompt.append("==============================")
        prompt.append(
            self._safe(context.user_input)
        )

        return "\n".join(prompt)