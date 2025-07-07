"""Core todo functionality."""


class Todo:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return Todo(title)
