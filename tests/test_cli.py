"""Tests for CLI functionality."""

from tcr_todo.cli import main


def test_can_call_cli_main() -> None:
    """Test that we can call the CLI main function."""
    main()


def test_main_accepts_args_list() -> None:
    """Test that main can accept an args list."""
    main(["add", "buy milk"])


def test_main_handles_add_command() -> None:
    """Test that main can handle an add command."""
    main(["add", "buy milk"])
