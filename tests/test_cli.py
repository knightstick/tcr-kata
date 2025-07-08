"""Tests for CLI functionality."""

from tcr_todo.cli import AddCommand, ListCommand, CLI
from tcr_todo.core import TodoCore
from tcr_todo.repo import InMemoryRepo


def test_can_call_cli_main() -> None:
    """Test that we can call the CLI main function."""
    cli = CLI(TodoCore(InMemoryRepo()))
    cli.main()


def test_main_accepts_args_list() -> None:
    """Test that main can accept an args list."""
    cli = CLI(TodoCore(InMemoryRepo()))
    cli.main(["add", "buy milk"])


def test_main_handles_add_command() -> None:
    """Test that main can handle an add command."""
    cli = CLI(TodoCore(InMemoryRepo()))
    result = cli.main(["add", "buy milk"])
    assert result == "buy milk"


def test_run_with_add_command() -> None:
    """Test that run executes AddCommand correctly."""
    cli = CLI(TodoCore(InMemoryRepo()))
    command = AddCommand(title="buy milk")
    result = cli.run(command)
    assert result == "buy milk"


def test_run_with_list_command_type_checks() -> None:
    """Test that ListCommand type checks with run()."""
    cli = CLI(TodoCore(InMemoryRepo()))
    command = ListCommand()
    result: str = cli.run(command)
    assert isinstance(result, str)


def test_main_handles_list_command() -> None:
    """Test that main can handle a list command."""
    cli = CLI(TodoCore(InMemoryRepo()))
    result = cli.main(["list"])
    assert isinstance(result, str)
    assert result.startswith("[")
    assert result.endswith("]")


def test_add_then_list_integration() -> None:
    """Test that adding a todo then listing shows the added todo."""
    cli = CLI(TodoCore(InMemoryRepo()))

    # Get initial count
    initial_list = cli.main(["list"])

    # Add a todo
    add_result = cli.main(["add", "integration test todo"])
    assert add_result == "integration test todo"

    # List should now contain the new todo
    final_list = cli.main(["list"])
    assert "integration test todo" in final_list
    assert len(final_list) > len(initial_list)


def test_main_raises_error_for_unknown_command() -> None:
    """Test that main raises an error for unknown commands."""
    import pytest

    cli = CLI(TodoCore(InMemoryRepo()))
    with pytest.raises(ValueError, match="Unknown command"):
        cli.main(["unknown"])


def test_add_command_concatenates_multiple_strings() -> None:
    """Test that add command concatenates multiple string arguments."""
    cli = CLI(TodoCore(InMemoryRepo()))
    result = cli.main(["add", "buy", "milk"])
    assert result == "buy milk"


def test_main_handles_empty_args() -> None:
    """Test that main handles empty args gracefully."""
    cli = CLI(TodoCore(InMemoryRepo()))
    result = cli.main([])
    assert result is None


def test_cli_class_with_inmemory_repo() -> None:
    """Test CLI class with InMemoryRepo for isolation."""
    repo = InMemoryRepo()
    todo_core = TodoCore(repo)
    cli = CLI(todo_core)

    # Test adding a todo
    add_result = cli.main(["add", "test task"])
    assert add_result == "test task"

    # Test listing todos
    list_result = cli.main(["list"])
    assert "test task" in list_result
