from core.context import AuraContext


class PromptBuilder:

    def build(self, context: AuraContext) -> str:

        prompt = []

        prompt.append("==============================")
        prompt.append("AURA INTERNAL CONTEXT")
        prompt.append("==============================")

        if context.profile:
            prompt.append("")
            prompt.append("[PROFILE]")
            prompt.append(f"Nama: {context.profile}")

        if context.memories:
            prompt.append("")
            prompt.append("[MEMORY]")

            for memory in context.memories:
                prompt.append(f"- {memory['memory_value']}")

        if context.emotion:
            prompt.append("")
            prompt.append("[EMOTION]")
            prompt.append(
                f"Emosi terakhir: {context.emotion['emotion']}"
            )
            prompt.append(
                f"Intensitas: {context.emotion['intensity']}"
            )

        if context.temporal:
            prompt.append("")
            prompt.append("[TEMPORAL CONTEXT]")

            for event in context.temporal:
                prompt.append(
                    f"- {event['event_type']}: "
                    f"{event['subject']} = {event['value']}"
                )

        if context.reflections:
            prompt.append("")
            prompt.append("[REFLECTION]")

            for reflection in context.reflections:
                prompt.append(
                    f"- {reflection['summary']}"
                )

        if context.history:
            prompt.append("")
            prompt.append("[RECENT CONVERSATION]")

            for chat in context.history:
                prompt.append(
                    f"{chat['role']}: {chat['message']}"
                )

        prompt.append("")
        prompt.append("==============================")
        prompt.append("CURRENT USER MESSAGE")
        prompt.append("==============================")
        prompt.append(context.user_input)

        return "\n".join(prompt)
