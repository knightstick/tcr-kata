"""Core todo functionality."""

from typing import Callable

from tcr_todo.models import Todo
from tcr_todo.repo import store_todo, retrieve_todos

StoreTodoFunction = Callable[[Todo], None]
RetrieveTodosFunction = Callable[[], list[Todo]]


def _add_todo(title: str, store: StoreTodoFunction | None = None) -> Todo:
    """Add a todo item (internal)."""
    todo = Todo(title)
    if store:
        store(todo)
    return todo


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return _add_todo(title, store_todo)


def _list_todos(retrieve: RetrieveTodosFunction | None = None) -> list[Todo]:
    """List all todo items (internal)."""
    if retrieve:
        return retrieve()
    return []


def list_todos() -> list[Todo]:
    """List all todo items."""
    return _list_todos(retrieve_todos)
