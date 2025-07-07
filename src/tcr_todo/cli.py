"""Command line interface for tcr_todo."""

import argparse
from dataclasses import dataclass

from tcr_todo.core import add_todo


@dataclass
class AddCommand:
    """Command to add a todo."""

    title: str


CLIArgs = AddCommand


def run(args: CLIArgs) -> str:
    """Execute CLI command with structured args."""
    todo = add_todo(args.title)
    return str(todo)


def cli_add(title: str) -> str:
    """Add a todo with the given title."""
    todo = add_todo(title)
    return str(todo)


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
