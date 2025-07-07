# TCR Kata: Command Line TODO List

## Goals

An experiment with Kent Beck's Test && Commit || Revert flow, building a deliberately under-specified command line TODO list application. The goal is to explore emergent design through TDD and TCR, keeping focused on the next clear step while tracking distractions separately (Kent Beck style from TDD by Example).

## Tech Choices

- **Language**: Python with strict typing
- **Auto-formatting**: Will be configured
- **Testing**: pytest
- **TCR Flow**: Manual test-commit-revert cycle
- **Note Keeping**: Separate distractions file

## What is TCR?

TCR (Test && Commit || Revert) is a development practice where:
- If tests pass → automatically commit
- If tests fail → automatically revert to last working state

**Origins:** Created by Kent Beck, Lars Barlindhaug, Oddmund Strømme, and Ole Johannessen during "Limbo on the Cheap" experiments. Kent Beck introduced "test && commit", and Oddmund Strømme suggested adding "|| revert" for symmetry.

**Key Benefits:**
- Forces extremely small, incremental steps
- Provides immediate feedback on code changes
- Increases test coverage and discipline
- Makes developers more conscious of their coding process

**Basic Command:** `<test command> && git commit -am "TCR" || git restore`

## The Challenge

Build a "command line TODO list" - intentionally vague to explore emergent design through TDD and TCR.

## Setup

```bash
# Install dependencies
poetry install

# Use the CLI
poetry run todo add "buy milk"
poetry run todo list

# Or use the bash wrapper
./bin/todo add "buy milk"
./bin/todo list
```

## Current Status

✅ **Working CLI with add/list commands**
- Clean command-line interface
- Type-safe architecture with dependency injection
- Ready for persistence implementation