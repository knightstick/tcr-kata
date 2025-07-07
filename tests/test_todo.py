"""Tests for todo functionality."""

from tcr_todo.core import add_todo, Todo


def test_true_is_truthy() -> None:
    """Test that true is truthy."""
    assert True


def test_can_import_core() -> None:
    """Test that we can import from tcr_todo.core."""
    import tcr_todo.core


def test_can_call_add_todo() -> None:
    """Test that we can call add_todo function."""
    result = add_todo("buy milk")
    assert result == "buy milk"


def test_can_create_todo() -> None:
    """Test that we can create a Todo object."""
    todo = Todo("buy milk")
    assert todo.text == "buy milk"
