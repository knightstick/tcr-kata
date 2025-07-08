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
