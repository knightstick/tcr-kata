"""Tests for todo functionality."""

from tcr_todo.core import add_todo, _list_todos, list_todos_from_repo, Todo
from tcr_todo.repo import InMemoryRepo, FileRepo


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


def test_repos_work_with_protocol() -> None:
    """Test that both InMemoryRepo and FileRepo work with TodoRepository protocol."""
    # InMemoryRepo
    memory_repo = InMemoryRepo()
    memory_repo.store_todo(Todo("memory task"))

    result = list_todos_from_repo(memory_repo)
    assert len(result.todos) == 1
    assert result.todos[0].title == "memory task"

    # FileRepo (without temp file for simplicity - just test it accepts the protocol)
    file_repo = FileRepo("test.json")
    result = list_todos_from_repo(file_repo)  # Should return empty list
    assert len(result.todos) == 0
