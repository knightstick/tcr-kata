"""Command line interface for tcr_todo."""

import argparse
import sys
from dataclasses import dataclass

from tcr_todo.core import TodoCore
from tcr_todo.repo import FileRepo


@dataclass
class AddCommand:
    """Command to add a todo."""

    title: str


@dataclass
class ListCommand:
    """Command to list todos."""

    pass


CLIArgs = AddCommand | ListCommand


class CLI:
    """CLI with dependency injection."""

    def __init__(self, todo_core: TodoCore) -> None:
        """Initialize with a TodoCore instance."""
        self.todo_core = todo_core

    def run(self, args: CLIArgs) -> str:
        """Execute CLI command with structured args."""
        match args:
            case AddCommand(title=title):
                todo = self.todo_core.add_todo(title)
                return str(todo)
            case ListCommand():
                todos = self.todo_core.list_todos()
                return str(todos)
            case _:
                raise ValueError(f"Unknown command: {args}")

    def main(self, args: list[str] | None = None) -> str | None:
        """Main CLI entry point."""
        match args:
            case None | []:
                return None
            case ["add", *title_parts]:
                title = " ".join(title_parts)
                add_command = AddCommand(title=title)
                return self.run(add_command)
            case ["list"]:
                list_command = ListCommand()
                return self.run(list_command)
            case [command, *_]:
                raise ValueError(f"Unknown command: {command}")
            case _:
                return None


# Initialize TodoCore with FileRepo
_todo_core = TodoCore(FileRepo("todos.json"))


def run(args: CLIArgs) -> str:
    """Execute CLI command with structured args."""
    match args:
        case AddCommand(title=title):
            todo = _todo_core.add_todo(title)
            return str(todo)
        case ListCommand():
            todos = _todo_core.list_todos()
            return str(todos)
        case _:
            raise ValueError(f"Unknown command: {args}")


def main(args: list[str] | None = None) -> str | None:
    """Main CLI entry point."""
    match args:
        case None | []:
            return None
        case ["add", *title_parts]:
            title = " ".join(title_parts)
            add_command = AddCommand(title=title)
            return run(add_command)
        case ["list"]:
            list_command = ListCommand()
            return run(list_command)
        case [command, *_]:
            raise ValueError(f"Unknown command: {command}")
        case _:
            return None


def cli_main() -> None:
    """CLI entry point for poetry script."""
    todo_core = TodoCore(FileRepo("todos.json"))
    cli = CLI(todo_core)
    result = cli.main(sys.argv[1:])
    if result:
        print(result)


if __name__ == "__main__":
    cli_main()
