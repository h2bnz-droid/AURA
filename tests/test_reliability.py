from unittest.mock import Mock, patch

import pytest

from core.reliability import (
    RetryExhaustedError,
    run_with_fallback,
    run_with_retry,
)


def test_run_with_retry_returns_success():
    operation = Mock(return_value="success")

    result = run_with_retry(
        operation,
        max_retries=2,
        backoff_seconds=0,
    )

    assert result == "success"
    assert operation.call_count == 1


def test_run_with_retry_retries_then_succeeds():
    operation = Mock(
        side_effect=[
            RuntimeError("temporary failure"),
            RuntimeError("temporary failure"),
            "success",
        ]
    )

    result = run_with_retry(
        operation,
        max_retries=2,
        backoff_seconds=0,
    )

    assert result == "success"
    assert operation.call_count == 3


def test_run_with_retry_raises_after_exhaustion():
    operation = Mock(
        side_effect=RuntimeError("provider unavailable")
    )

    with pytest.raises(RetryExhaustedError):
        run_with_retry(
            operation,
            max_retries=2,
            backoff_seconds=0,
        )

    assert operation.call_count == 3


def test_run_with_retry_uses_exponential_backoff():
    operation = Mock(
        side_effect=[
            RuntimeError("temporary failure"),
            RuntimeError("temporary failure"),
            "success",
        ]
    )

    with patch("core.reliability.time.sleep") as sleep:
        result = run_with_retry(
            operation,
            max_retries=2,
            backoff_seconds=0.2,
        )

    assert result == "success"
    assert sleep.call_args_list[0].args == (0.2,)
    assert sleep.call_args_list[1].args == (0.4,)


def test_run_with_retry_rejects_invalid_operation():
    with pytest.raises(TypeError):
        run_with_retry("not callable")


def test_run_with_retry_rejects_negative_retries():
    with pytest.raises(ValueError):
        run_with_retry(lambda: "ok", max_retries=-1)


def test_run_with_retry_rejects_negative_backoff():
    with pytest.raises(ValueError):
        run_with_retry(lambda: "ok", backoff_seconds=-1)

def test_run_with_fallback_returns_operation_result():
    operation = Mock(return_value="saved")

    result = run_with_fallback(
        operation,
        fallback=None,
    )

    assert result == "saved"


def test_run_with_fallback_returns_fallback_on_error():
    operation = Mock(
        side_effect=RuntimeError("database unavailable")
    )

    result = run_with_fallback(
        operation,
        fallback=None,
    )

    assert result is None


def test_run_with_fallback_does_not_raise_operation_error():
    operation = Mock(
        side_effect=RuntimeError("database unavailable")
    )

    result = run_with_fallback(
        operation,
        fallback="safe result",
    )

    assert result == "safe result"