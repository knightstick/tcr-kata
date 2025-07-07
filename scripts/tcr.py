#!/usr/bin/env python3
"""TCR (Test && Commit || Revert) script."""

import subprocess
import sys
from datetime import datetime


def run_command(cmd: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"🔧 {description}...")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {description} failed")
        return False


def main() -> None:
    """Run the TCR workflow."""
    # Format
    if not run_command(["poetry", "run", "ruff", "format", "."], "Auto-formatting"):
        return

    # Type check (stop if fails)
    if not run_command(["poetry", "run", "mypy", "src/"], "Type checking"):
        return

    # Test && commit || revert
    print("🧪 Running tests...")
    if run_command(["poetry", "run", "pytest"], "Tests"):
        print("✅ Tests passed - committing...")
        subprocess.run(["git", "add", "."])
        subprocess.run(
            ["git", "commit", "-m", f"TCR: {datetime.now().strftime('%H:%M:%S')}"]
        )
    else:
        print("❌ Tests failed - reverting...")
        subprocess.run(["git", "restore", "."])


if __name__ == "__main__":
    main()
