"""Tests for todo functionality."""

from tcr_todo.core import add_todo, Todo


def test_add_todo_creates_todo_with_title() -> None:
    """Test that add_todo creates a Todo with the given title."""
    result = add_todo("buy milk")
    assert result.title == "buy milk"


def test_todo_stores_title() -> None:
    """Test that Todo stores the title."""
    todo = Todo("buy milk")
    assert todo.title == "buy milk"


def test_todo_has_string_representation() -> None:
    """Test that Todo can be converted to string."""
    todo = Todo("buy milk")
    str(todo)
