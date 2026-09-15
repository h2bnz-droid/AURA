from __future__ import annotations

import time
from collections.abc import Callable


DEFAULT_MAX_RETRIES = 2
DEFAULT_BACKOFF_SECONDS = 0.2


class RetryExhaustedError(RuntimeError):
    """Raised when all retry attempts have failed."""


def run_with_retry(
    operation: Callable,
    *,
    max_retries: int = DEFAULT_MAX_RETRIES,
    backoff_seconds: float = DEFAULT_BACKOFF_SECONDS,
    retryable_exceptions: tuple[type[Exception], ...] = (Exception,),
):
    """
    Run an operation with a bounded retry policy.
    """

    if not callable(operation):
        raise TypeError("Operation must be callable.")

    if max_retries < 0:
        raise ValueError("max_retries cannot be negative.")

    if backoff_seconds < 0:
        raise ValueError("backoff_seconds cannot be negative.")

    attempts = max_retries + 1
    last_error = None

    for attempt in range(attempts):
        try:
            return operation()
        except retryable_exceptions as exc:
            last_error = exc

            if attempt == attempts - 1:
                break

            delay = backoff_seconds * (2**attempt)

            if delay > 0:
                time.sleep(delay)

    raise RetryExhaustedError(
        "Operation failed after all retry attempts."
    ) from last_error

def run_with_fallback(
    operation: Callable,
    fallback,
):
    """
    Run an operation and return fallback if it fails.
    """

    if not callable(operation):
        raise TypeError("Operation must be callable.")

    try:
        return operation()
    except Exception:
        return fallback