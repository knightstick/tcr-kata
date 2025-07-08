"""Tests for FileRepo functionality."""

import os
import tempfile
from tcr_todo.models import Todo
from tcr_todo.repo import FileRepo


def test_file_repo_can_be_created() -> None:
    """Test that FileRepo can be instantiated."""
    repo = FileRepo("test.json")
    assert repo.filename == "test.json"
