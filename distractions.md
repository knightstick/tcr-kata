# Distractions

A place to capture ideas and tangents that come up during TCR development, inspired by Kent Beck's note-keeping style in "TDD by Example".

## Current Focus
✅ Building persistence layer with dependency injection - COMPLETE!

## Main Goal
✅ Create a todo from the command line - COMPLETE!

## Completed Session Goals
✅ Implement actual persistence in `repo.store_todo()` (in-memory list)
✅ Add `retrieve_todos()` function to repo
✅ Wire up `list_todos()` to use `retrieve_todos()`
✅ Test full add→list workflow with persistence
✅ Better formatting for list output (TodoList container)
✅ Clean up "Todo" type annotations (all good, no forward references needed)
✅ todocli unknown should raise an error (ValueError with helpful message)

## Parking Lot
- Ideas and questions that come up during development
- Things to explore later
- Refactoring opportunities
- Architecture decisions to revisit
- Todos can have optional descriptions

## Decisions
- Use `argparse` for CLI argument parsing (built-in, no dependencies, easy to test with args list)

## Notes
- When running TCR script, narrate the red/green feedback for user visibility (format ✅/❌, type check ✅/❌, tests ✅/❌)

---

*"Keep focused on the next clear step while tracking distractions separately."*