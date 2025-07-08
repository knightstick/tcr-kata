"""Command line interface for tcr_todo."""

import argparse
import sys
from dataclasses import dataclass

from tcr_todo.core import add_todo, list_todos


@dataclass
class AddCommand:
    """Command to add a todo."""

    title: str


@dataclass
class ListCommand:
    """Command to list todos."""

    pass


CLIArgs = AddCommand | ListCommand


def run(args: CLIArgs) -> str:
    """Execute CLI command with structured args."""
    match args:
        case AddCommand(title=title):
            todo = add_todo(title)
            return str(todo)
        case ListCommand():
            todos = list_todos()
            return str(todos)
        case _:
            raise ValueError(f"Unknown command: {args}")


def main(args: list[str] | None = None) -> str | None:
    """Main CLI entry point."""
    if not args:
        return None

    command = args[0]
    if command == "add":
        title = " ".join(args[1:])
        add_command = AddCommand(title=title)
        return run(add_command)
    elif command == "list":
        list_command = ListCommand()
        return run(list_command)
    else:
        raise ValueError(f"Unknown command: {command}")


def cli_main() -> None:
    """CLI entry point for poetry script."""
    result = main(sys.argv[1:])
    if result:
        print(result)


if __name__ == "__main__":
    cli_main()
