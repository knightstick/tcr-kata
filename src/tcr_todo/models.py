"""Todo domain models."""


class Todo:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title

    def __str__(self) -> str:
        """Return string representation of todo."""
        return self.title


class TodoList:
    """A container for todo items that knows how to display itself."""

    def __init__(self, todos: list[Todo]) -> None:
        """Initialize with a list of todos."""
        self.todos = todos

    def __str__(self) -> str:
        """Return formatted string representation of the todo list."""
        return str([str(todo) for todo in self.todos])
