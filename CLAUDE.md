# Claude Instructions

## TCR Workflow

When running the TCR script, always provide clear red/green feedback to the user:

```
Running TCR...
🔧 Format: ✅ 
🔍 Type check: ✅
🧪 Tests: ❌ FAILED - reverting changes
```

Or for success:
```
Running TCR...
🔧 Format: ✅ 
🔍 Type check: ✅
🧪 Tests: ✅ PASSED - committing changes
```

This ensures the user gets immediate visual feedback about each step of the TCR process, maintaining the important red/green feedback loop that's core to TDD and TCR workflows.

## Distractions File

Use `distractions.md` for Kent Beck style note-keeping:
- Track ideas and tangents that come up during development
- Note things to explore later
- Record refactoring opportunities
- Keep architecture decisions to revisit
- Maintain focus on the current clear next step
- When you add a distraction, commit it straight away

## TCR Learning

- When the TCR fails, I want to know what we LOST and what we LEARNED