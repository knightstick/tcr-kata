"""Command line interface for tcr_todo."""

import argparse
from dataclasses import dataclass

from tcr_todo.core import add_todo


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
    if isinstance(args, AddCommand):
        todo = add_todo(args.title)
        return str(todo)
    elif isinstance(args, ListCommand):
        return "No todos yet"  # Placeholder
    else:
        raise ValueError(f"Unknown command: {args}")


def main(args: list[str] | None = None) -> str | None:
    """Main CLI entry point."""
    if not args:
        return None

    command = args[0]
    if command == "add":
        title = args[1]
        add_command = AddCommand(title=title)
        return run(add_command)

    return None


if __name__ == "__main__":
    main()
