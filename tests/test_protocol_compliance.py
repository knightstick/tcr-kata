"""Tests for Protocol compliance using type checking."""

import tempfile
from pathlib import Path
from tcr_todo.repo import InMemoryRepo, FileRepo, SQLiteRepo, TodoRepository


def test_repos_satisfy_protocol() -> None:
    """Test that repo implementations satisfy TodoRepository protocol.

    If these assignments compile without mypy errors, the Protocol is satisfied.
    This is the main value of Protocols - static type checking guarantees.
    """
    # Type checker verifies these assignments are valid
    _memory_repo: TodoRepository = InMemoryRepo()
    _file_repo: TodoRepository = FileRepo("test.json")

    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "test.db"
        _sqlite_repo: TodoRepository = SQLiteRepo(str(db_path))

    # That's it! Mypy guarantees everything we need.
