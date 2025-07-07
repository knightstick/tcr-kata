"""Command line interface for tcr_todo."""

import argparse


def main(args: list[str] | None = None) -> None:
    """Main CLI entry point."""
    if not args:
        return

    command = args[0]
    if command == "add":
        pass  # TODO: handle add command


if __name__ == "__main__":
    main()
