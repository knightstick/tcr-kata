"""Todo repository functions."""

from tcr_todo.models import Todo

# In-memory storage for todos
_todos: list[Todo] = []


def store_todo(todo: Todo) -> None:
    """Store a todo item."""
    _todos.append(todo)
