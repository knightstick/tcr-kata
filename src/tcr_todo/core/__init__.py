"""Core todo functionality."""

from typing import Callable

from tcr_todo.models import Todo
from tcr_todo.repo import fake_store_todo as repo_fake_store_todo

StoreTodoFunction = Callable[[Todo], None]


def _add_todo(title: str, store: StoreTodoFunction | None = None) -> Todo:
    """Add a todo item (internal)."""
    todo = Todo(title)
    if store:
        store(todo)
    return todo


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return _add_todo(title, repo_fake_store_todo)


def list_todos() -> list[Todo]:
    """List all todo items."""
    return []
