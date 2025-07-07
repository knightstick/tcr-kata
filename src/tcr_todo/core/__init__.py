"""Core todo functionality."""

from typing import Callable


StoreTodoFunction = Callable[["Todo"], None]


class Todo:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title

    def __str__(self) -> str:
        """Return string representation of todo."""
        return self.title


def _add_todo(title: str, store: StoreTodoFunction | None = None) -> Todo:
    """Add a todo item (internal)."""
    todo = Todo(title)
    if store:
        store(todo)
    return todo


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return _add_todo(title)


def fake_store_todo(todo: "Todo") -> None:
    """Fake store function that does nothing."""
    pass


def list_todos() -> list[Todo]:
    """List all todo items."""
    return []
