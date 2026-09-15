from __future__ import annotations


DEFAULT_FALLBACK_RESPONSE = (
    "Maaf, AURA sedang mengalami kendala sementara. "
    "Silakan coba lagi beberapa saat."
)


def get_fallback_response() -> str:
    """
    Return a safe response when the AI provider is unavailable.
    """

    return DEFAULT_FALLBACK_RESPONSE
