"""Tests for CLI functionality."""

from tcr_todo.cli import main, run, AddCommand, ListCommand


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


def test_run_with_list_command_type_checks() -> None:
    """Test that ListCommand type checks with run()."""
    command = ListCommand()
    result: str = run(
        command
    )  # Type checker will fail if run() can't handle ListCommand


def test_main_handles_list_command() -> None:
    """Test that main can handle a list command."""
    result = main(["list"])
    assert isinstance(result, str)
    assert result.startswith("[")
    assert result.endswith("]")
