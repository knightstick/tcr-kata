"""Todo repository implementations and Protocol."""

from typing import Protocol
from tcr_todo.models import Todo


class TodoRepository(Protocol):
    """Protocol defining the interface for todo repositories."""

    def store_todo(self, todo: Todo) -> None:
        """Store a todo item."""
        ...

    def retrieve_todos(self) -> list[Todo]:
        """Retrieve all stored todos."""
        ...


# Import and re-export all repository implementations
from .memory import InMemoryRepo
from .file import FileRepo
from .sqlite import SQLiteRepo

__all__ = ["TodoRepository", "InMemoryRepo", "FileRepo", "SQLiteRepo"]
