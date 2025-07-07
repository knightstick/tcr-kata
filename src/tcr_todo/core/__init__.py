"""Core todo functionality."""


class Todo:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title

    def __str__(self) -> str:
        """Return string representation of todo."""
        return self.title


def _add_todo(title: str) -> Todo:
    """Add a todo item (internal)."""
    return Todo(title)


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return _add_todo(title)


def list_todos() -> list[Todo]:
    """List all todo items."""
    return []
