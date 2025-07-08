"""Tests for SQLite repository."""

import tempfile
from pathlib import Path
from tcr_todo.models import Todo
from tcr_todo.repo import SQLiteRepo, TodoRepository


def test_sqlite_repo_can_be_created() -> None:
    """Test that SQLiteRepo can be created."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo = SQLiteRepo(str(db_path))
        assert repo.db_path == str(db_path)


def test_store_and_retrieve_single_todo() -> None:
    """Test storing and retrieving a single todo."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo = SQLiteRepo(str(db_path))

        # Store a todo
        todo = Todo("test task")
        repo.store_todo(todo)

        # Retrieve todos
        todos = repo.retrieve_todos()
        assert len(todos) == 1
        assert todos[0].title == "test task"


def test_store_multiple_todos() -> None:
    """Test storing and retrieving multiple todos."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo = SQLiteRepo(str(db_path))

        # Store multiple todos
        todo1 = Todo("first task")
        todo2 = Todo("second task")
        repo.store_todo(todo1)
        repo.store_todo(todo2)

        # Retrieve todos
        todos = repo.retrieve_todos()
        assert len(todos) == 2
        assert todos[0].title == "first task"
        assert todos[1].title == "second task"


def test_retrieve_todos_returns_empty_for_new_db() -> None:
    """Test that retrieve_todos returns empty list for new database."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo = SQLiteRepo(str(db_path))

        todos = repo.retrieve_todos()
        assert todos == []


def test_sqlite_repo_satisfies_protocol() -> None:
    """Test that SQLiteRepo satisfies TodoRepository protocol."""
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        repo: TodoRepository = SQLiteRepo(str(db_path))

        # Type checker will verify this assignment is valid
        # If SQLiteRepo doesn't satisfy the protocol, mypy will complain
        assert hasattr(repo, "store_todo")
        assert hasattr(repo, "retrieve_todos")
        assert callable(repo.store_todo)
        assert callable(repo.retrieve_todos)
