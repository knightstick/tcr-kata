"""Command line interface for tcr_todo."""

import argparse

from tcr_todo.core import add_todo


def main(args: list[str] | None = None) -> None:
    """Main CLI entry point."""
    if not args:
        return

    command = args[0]
    if command == "add":
        title = args[1]
        add_todo(title)


if __name__ == "__main__":
    main()
