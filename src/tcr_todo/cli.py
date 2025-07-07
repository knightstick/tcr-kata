"""Command line interface for tcr_todo."""

import argparse

from tcr_todo.core import add_todo


def main(args: list[str] | None = None) -> str | None:
    """Main CLI entry point."""
    if not args:
        return None

    command = args[0]
    if command == "add":
        title = args[1]
        todo = add_todo(title)
        return str(todo)

    return None


if __name__ == "__main__":
    main()
