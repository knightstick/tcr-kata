"""Tests for FileRepo functionality."""

import os
import tempfile
from tcr_todo.models import Todo
from tcr_todo.repo import FileRepo


def test_file_repo_can_be_created() -> None:
    """Test that FileRepo can be instantiated."""
    repo = FileRepo("test.json")
    assert repo.filename == "test.json"


def test_retrieve_todos_returns_empty_for_nonexistent_file() -> None:
    """Test that retrieve_todos returns empty list when file doesn't exist."""
    repo = FileRepo("nonexistent_file.json")
    todos = repo.retrieve_todos()
    assert todos == []
