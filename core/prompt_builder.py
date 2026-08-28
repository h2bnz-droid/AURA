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

        if context.relationships:
            prompt.append("")
            prompt.append("[RELATIONSHIP]")

            for relationship in context.relationships:
                prompt.append(
                    f"- {relationship['person_name']}: "
                    f"{relationship['relationship_type']}"
                )

        if context.cognitive_model:
            prompt.append("")
            prompt.append("[PERSONAL COGNITIVE MODEL]")

            for attribute in context.cognitive_model:
                prompt.append(
                    f"- {attribute['attribute_name']}: "
                    f"{attribute['attribute_value']}"
                )

        if context.personalization:
            prompt.append("")
            prompt.append("[PERSONALIZATION]")

            for name, value in context.personalization.items():
                prompt.append(
                    f"- {name}: {value}"
                )

        if context.long_term_context:
            prompt.append("")
            prompt.append("[LONG-TERM CONTEXT]")

            for item in context.long_term_context:
                prompt.append(
                    f"- {item['content']}"
                )

        if context.integrated_cognitive_context:
            items = context.integrated_cognitive_context.all_items()

            if items:
                prompt.append("")
                prompt.append("[INTEGRATED COGNITIVE CONTEXT]")

                for item in items:
                    prompt.append(
                        f"- {item.category}: {item.value}"
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
