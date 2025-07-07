"""Tests for CLI functionality."""

from tcr_todo.cli import main, cli_add


def test_can_call_cli_main() -> None:
    """Test that we can call the CLI main function."""
    main()


def test_main_accepts_args_list() -> None:
    """Test that main can accept an args list."""
    main(["add", "buy milk"])


def test_main_handles_add_command() -> None:
    """Test that main can handle an add command."""
    result = main(["add", "buy milk"])
    assert isinstance(result, str)


def test_cli_add_returns_todo_string() -> None:
    """Test that cli_add returns a string representation of the todo."""
    result = cli_add("buy milk")
    assert result == "buy milk"
