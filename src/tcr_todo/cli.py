"""Command line interface for tcr_todo."""

import argparse

from tcr_todo.core import add_todo


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
        return cli_add(title)

    return None


if __name__ == "__main__":
    main()
