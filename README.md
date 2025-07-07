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

**Key Benefits:**
- Forces extremely small, incremental steps
- Provides immediate feedback on code changes
- Increases test coverage and discipline
- Makes developers more conscious of their coding process

**Basic Command:** `<test command> && git commit -am "TCR" || git restore`

## The Challenge

Build a "command line TODO list" - intentionally vague to explore emergent design through TDD and TCR.

## Setup

TODO: Add setup instructions as we build them

## Current Status

Starting the experiment...