"""Tests for CLI functionality."""

from tcr_todo.cli import main, run, AddCommand


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


def test_run_with_add_command() -> None:
    """Test that run executes AddCommand correctly."""
    command = AddCommand(title="buy milk")
    result = run(command)
    assert result == "buy milk"
