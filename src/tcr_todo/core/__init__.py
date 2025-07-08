"""Core todo functionality."""

from typing import Callable

from tcr_todo.models import Todo, TodoList
from tcr_todo.repo import InMemoryRepo, TodoRepository

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
