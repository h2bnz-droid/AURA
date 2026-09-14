from __future__ import annotations

import ollama

from core.config import MODEL
from core.security import redact_sensitive_data


class AIProviderError(RuntimeError):
    """Raised when the AI provider cannot generate a response."""


def chat(messages):
    safe_messages = _sanitize_messages(messages)

    try:
        response = ollama.chat(
            model=MODEL,
            messages=safe_messages,
        )
    except Exception as exc:
        raise AIProviderError(
            "AI provider failed to generate a response."
        ) from exc

    if not isinstance(response, dict):
        raise AIProviderError(
            "AI provider returned an invalid response."
        )

    message = response.get("message")

    if not isinstance(message, dict):
        raise AIProviderError(
            "AI provider response is missing message data."
        )

    content = message.get("content")

    if not isinstance(content, str) or not content.strip():
        raise AIProviderError(
            "AI provider response is missing content."
        )

    return content


def _sanitize_messages(messages):
    """
    Sanitize message content before sending it to the AI provider.
    """

    if not isinstance(messages, list):
        raise AIProviderError(
            "AI provider messages must be a list."
        )

    safe_messages = []

    for message in messages:
        if not isinstance(message, dict):
            raise AIProviderError(
                "AI provider message must be a dictionary."
            )

        safe_message = dict(message)

        if "content" in safe_message:
            safe_message["content"] = redact_sensitive_data(
                str(safe_message["content"])
            )

        safe_messages.append(safe_message)

    return safe_messages