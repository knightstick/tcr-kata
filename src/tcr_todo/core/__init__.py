"""Core todo functionality."""

from typing import Callable

from tcr_todo.models import Todo, TodoList
from tcr_todo.repo import FileRepo, TodoRepository


class TodoCore:
    """Core todo functionality with dependency injection."""

    def __init__(self, repo: TodoRepository) -> None:
        """Initialize with a todo repository."""
        self.repo = repo

    def add_todo(self, title: str) -> Todo:
        """Add a todo item."""
        todo = Todo(title)
        self.repo.store_todo(todo)
        return todo

    def list_todos(self) -> TodoList:
        """List all todo items."""
        todos = self.repo.retrieve_todos()
        return TodoList(todos)


# Legacy type aliases - kept for backward compatibility with _add_todo/_list_todos
StoreTodoFunction = Callable[[Todo], None]
RetrieveTodosFunction = Callable[[], list[Todo]]

# Default repo instance
_default_repo = FileRepo("todos.json")


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
