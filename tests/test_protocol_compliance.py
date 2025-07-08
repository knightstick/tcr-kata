"""Tests for Protocol compliance using type checking."""

from tcr_todo.repo import InMemoryRepo, FileRepo, TodoRepository


def test_repos_satisfy_protocol() -> None:
    """Test that repo implementations satisfy TodoRepository protocol.

    If these assignments compile without mypy errors, the Protocol is satisfied.
    This is the main value of Protocols - static type checking guarantees.
    """
    # Type checker verifies these assignments are valid
    memory_repo: TodoRepository = InMemoryRepo()
    file_repo: TodoRepository = FileRepo("test.json")

    # Mypy guarantees these have the right methods with correct signatures
    assert callable(memory_repo.store_todo)
    assert callable(memory_repo.retrieve_todos)
    assert callable(file_repo.store_todo)
    assert callable(file_repo.retrieve_todos)
