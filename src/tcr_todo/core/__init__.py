"""Core todo functionality."""


class Todo:
    """A todo item."""

    def __init__(self, text: str) -> None:
        """Initialize a todo with text."""
        self.text = text


def add_todo(text: str) -> str:
    """Add a todo item."""
    return text
