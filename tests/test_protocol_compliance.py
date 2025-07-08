"""Tests for Protocol compliance using type checking."""

from tcr_todo.repo import InMemoryRepo, FileRepo, TodoRepository


def test_repos_satisfy_protocol() -> None:
    """Test that repo implementations satisfy TodoRepository protocol.

    If these assignments compile without mypy errors, the Protocol is satisfied.
    This is the main value of Protocols - static type checking guarantees.
    """
    # Type checker verifies these assignments are valid
    _memory_repo: TodoRepository = InMemoryRepo()
    _file_repo: TodoRepository = FileRepo("test.json")

    # That's it! Mypy guarantees everything we need.
