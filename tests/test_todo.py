"""Tests for todo functionality."""

from tcr_todo.core import add_todo


def test_true_is_truthy() -> None:
    """Test that true is truthy."""
    assert True


def test_can_import_core() -> None:
    """Test that we can import from tcr_todo.core."""
    import tcr_todo.core


def test_can_call_add_todo() -> None:
    """Test that we can call add_todo function."""
    add_todo("buy milk")
