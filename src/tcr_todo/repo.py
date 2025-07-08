"""Todo repository implementations and Protocol."""

import json
import os
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


class InMemoryRepo:
    """In-memory todo repository."""

    def __init__(self) -> None:
        """Initialize with empty todo list."""
        self._todos: list[Todo] = []

    def store_todo(self, todo: Todo) -> None:
        """Store a todo item."""
        self._todos.append(todo)

    def retrieve_todos(self) -> list[Todo]:
        """Retrieve all stored todos."""
        return self._todos.copy()


class FileRepo:
    """File-based todo repository using JSON."""

    def __init__(self, filename: str) -> None:
        """Initialize with filename for storage."""
        self.filename = filename

    def store_todo(self, todo: Todo) -> None:
        """Store a todo item to file."""
        # Read existing todos
        todos = self.retrieve_todos()

        # Add new todo
        todos.append(todo)

        # Convert to JSON format
        data = [{"title": t.title} for t in todos]

        # Write back to file
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def retrieve_todos(self) -> list[Todo]:
        """Retrieve todos from file."""
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

        todos = []
        for item in data:
            todo = Todo(item["title"])
            todos.append(todo)

        return todos
