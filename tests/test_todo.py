"""Tests for todo functionality."""

import tempfile
from pathlib import Path
from tcr_todo.core import TodoCore
from tcr_todo.models import Todo
from tcr_todo.repo import InMemoryRepo, FileRepo, SQLiteRepo, TodoRepository


def test_add_todo_creates_todo_with_title() -> None:
    """Test that TodoCore.add_todo creates a Todo with the given title."""
    core = TodoCore(InMemoryRepo())
    result = core.add_todo("buy milk")
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
    """Test that TodoCore.list_todos uses the provided repo."""
    expected_todos = [Todo("task 1"), Todo("task 2")]

    repo = InMemoryRepo()
    for todo in expected_todos:
        repo.store_todo(todo)

    core = TodoCore(repo)
    result = core.list_todos()
    assert result.todos == expected_todos


def test_repos_work_with_protocol() -> None:
    """Test that both InMemoryRepo and FileRepo work with TodoRepository protocol."""
    # InMemoryRepo
    memory_repo = InMemoryRepo()
    memory_core = TodoCore(memory_repo)
    memory_core.add_todo("memory task")

    result = memory_core.list_todos()
    assert len(result.todos) == 1
    assert result.todos[0].title == "memory task"

    # FileRepo (without temp file for simplicity - just test it accepts the protocol)
    file_repo = FileRepo("test.json")
    file_core = TodoCore(file_repo)
    result = file_core.list_todos()  # Should return empty list
    assert len(result.todos) == 0


def test_inmemory_repo_satisfies_protocol() -> None:
    """Test that InMemoryRepo satisfies TodoRepository protocol."""
    repo: TodoRepository = InMemoryRepo()

    # Type checker will verify this assignment is valid
    # If InMemoryRepo doesn't satisfy the protocol, mypy will complain
    assert hasattr(repo, "store_todo")
    assert hasattr(repo, "retrieve_todos")
    assert callable(repo.store_todo)
    assert callable(repo.retrieve_todos)


def test_todo_core_with_inmemory_repo() -> None:
    """Test TodoCore with InMemoryRepo."""
    repo = InMemoryRepo()
    core = TodoCore(repo)

    # Add a todo
    todo = core.add_todo("test task")
    assert todo.title == "test task"

    # List todos
    result = core.list_todos()
    assert len(result.todos) == 1
    assert result.todos[0].title == "test task"


def test_todo_core_with_sqlite_repo() -> None:
    """Test TodoCore with SQLiteRepo."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo = SQLiteRepo(str(db_path))
        core = TodoCore(repo)

        # Add a todo
        todo = core.add_todo("sqlite test task")
        assert todo.title == "sqlite test task"

        # List todos
        result = core.list_todos()
        assert len(result.todos) == 1
        assert result.todos[0].title == "sqlite test task"
