"""Core todo functionality."""

from typing import Callable

from tcr_todo.models import Todo, TodoList
from tcr_todo.repo import InMemoryRepo, TodoRepository


class TodoCore:
    """A todo item."""

    def __init__(self, title: str) -> None:
        """Initialize a todo with title."""
        self.title = title

    def __str__(self) -> str:
        """Return string representation of todo."""
        return self.title


class TodoListCore:
    """A container for todo items that knows how to display itself."""

    def __init__(self, todos: list[TodoCore]) -> None:
        """Initialize with a list of todos."""
        self.todos = todos

    def __str__(self) -> str:
        """Return formatted string representation of the todo list."""
        return str([str(todo) for todo in self.todos])


# Legacy type aliases - kept for backward compatibility with _add_todo/_list_todos
StoreTodoFunction = Callable[[Todo], None]
RetrieveTodosFunction = Callable[[], list[Todo]]

# Default repo instance
_default_repo = InMemoryRepo()


def _add_todo(title: str, store: StoreTodoFunction | None = None) -> Todo:
    """Add a todo item (internal)."""
    todo = Todo(title)
    if store:
        store(todo)
    return todo


def add_todo(title: str) -> Todo:
    """Add a todo item."""
    return _add_todo(title, _default_repo.store_todo)


def _list_todos(retrieve: RetrieveTodosFunction | None = None) -> list[Todo]:
    """List all todo items (internal)."""
    if retrieve:
        return retrieve()
    return []


def list_todos() -> TodoList:
    """List all todo items."""
    todos = _list_todos(_default_repo.retrieve_todos)
    return TodoList(todos)


def list_todos_from_repo(repo: TodoRepository) -> TodoList:
    """List all todo items from a specific repository."""
    todos = _list_todos(repo.retrieve_todos)
    return TodoList(todos)


def create_todo_core(title: str) -> TodoCore:
    """Create a new TodoCore instance."""
    return TodoCore(title)
