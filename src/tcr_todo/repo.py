"""Todo repository functions."""

from tcr_todo.models import Todo

# In-memory storage for todos
_todos: list[Todo] = []


def store_todo(todo: Todo) -> None:
    """Store a todo item."""
    _todos.append(todo)


def retrieve_todos() -> list[Todo]:
    """Retrieve all stored todos."""
    return _todos.copy()


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
        pass  # TODO: implement

    def retrieve_todos(self) -> list[Todo]:
        """Retrieve todos from file."""
        return []  # TODO: implement
