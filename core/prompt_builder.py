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
    
        profile = profile_engine.get_profile()