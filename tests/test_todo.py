"""Tests for todo functionality."""

from tcr_todo.core import add_todo, _list_todos, Todo


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
    result = str(todo)
    assert "buy milk" in result


def test_list_todos_with_fake_repo() -> None:
    """Test that _list_todos uses the provided retrieve function."""
    expected_todos = [Todo("task 1"), Todo("task 2")]

    def fake_retrieve() -> list[Todo]:
        return expected_todos

    result = _list_todos(fake_retrieve)
    assert result == expected_todos
