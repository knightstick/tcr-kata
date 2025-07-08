"""Tests for FileRepo functionality."""

import os
import tempfile
from tcr_todo.models import Todo
from tcr_todo.repo import FileRepo, TodoRepository


def test_file_repo_can_be_created() -> None:
    """Test that FileRepo can be instantiated."""
    repo = FileRepo("test.json")
    assert repo.filename == "test.json"


def test_retrieve_todos_returns_empty_for_nonexistent_file() -> None:
    """Test that retrieve_todos returns empty list when file doesn't exist."""
    repo = FileRepo("nonexistent_file.json")
    todos = repo.retrieve_todos()
    assert todos == []


def test_store_and_retrieve_single_todo() -> None:
    """Test storing and retrieving a single todo."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
        filename = f.name

    try:
        repo = FileRepo(filename)

        # Store a todo
        todo = Todo("test task")
        repo.store_todo(todo)

        # Retrieve and verify
        todos = repo.retrieve_todos()
        assert len(todos) == 1
        assert todos[0].title == "test task"

    finally:
        if os.path.exists(filename):
            os.unlink(filename)


def test_store_multiple_todos() -> None:
    """Test storing multiple todos."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as f:
        filename = f.name

    try:
        repo = FileRepo(filename)

        # Store multiple todos
        repo.store_todo(Todo("first task"))
        repo.store_todo(Todo("second task"))

        # Retrieve and verify
        todos = repo.retrieve_todos()
        assert len(todos) == 2
        assert todos[0].title == "first task"
        assert todos[1].title == "second task"

    finally:
        if os.path.exists(filename):
            os.unlink(filename)


def test_file_repo_satisfies_protocol() -> None:
    """Test that FileRepo satisfies TodoRepository protocol."""
    repo: TodoRepository = FileRepo("test.json")

    # Type checker will verify this assignment is valid
    # If FileRepo doesn't satisfy the protocol, mypy will complain
    assert hasattr(repo, "store_todo")
    assert hasattr(repo, "retrieve_todos")
    assert callable(repo.store_todo)
    assert callable(repo.retrieve_todos)
