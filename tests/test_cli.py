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


def test_add_then_list_integration() -> None:
    """Test that adding a todo then listing shows the added todo."""
    # Get initial count
    initial_list = main(["list"])

    # Add a todo
    add_result = main(["add", "integration test todo"])
    assert add_result == "integration test todo"

    # List should now contain the new todo
    final_list = main(["list"])
    assert "integration test todo" in final_list
    assert len(final_list) > len(initial_list)


def test_main_raises_error_for_unknown_command() -> None:
    """Test that main raises an error for unknown commands."""
    import pytest

    with pytest.raises(ValueError, match="Unknown command"):
        main(["unknown"])
