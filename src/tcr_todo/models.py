"""Todo domain models."""


class Todo:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title

    def __str__(self) -> str:
        """Return string representation of todo."""
        return self.title
