"""Tests for todo functionality."""

from tcr_todo.core import add_todo, Todo


def test_can_call_add_todo() -> None:
    """Test that we can call add_todo function."""
    result = add_todo("buy milk")
    assert result.title == "buy milk"


def test_can_create_todo() -> None:
    """Test that we can create a Todo object."""
    todo = Todo("buy milk")
    assert todo.title == "buy milk"
