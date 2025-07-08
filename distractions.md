# Distractions

A place to capture ideas and tangents that come up during TCR development, inspired by Kent Beck's note-keeping style in "TDD by Example".

## Current Focus
✅ SQLiteRepo with production-grade database persistence - COMPLETE!

## Previous Goals
✅ Create a todo from the command line - COMPLETE!
✅ Building persistence layer with dependency injection - COMPLETE!
✅ FileRepo with JSON persistence - COMPLETE!

## Completed Session Goals
✅ Implement actual persistence in `repo.store_todo()` (in-memory list)
✅ Add `retrieve_todos()` function to repo
✅ Wire up `list_todos()` to use `retrieve_todos()`
✅ Test full add→list workflow with persistence
✅ Better formatting for list output (TodoList container)
✅ Clean up "Todo" type annotations (all good, no forward references needed)
✅ todocli unknown should raise an error (ValueError with helpful message)
✅ Multiple argument concatenation for add command (user-friendly)
✅ Pattern matching for main CLI parsing (cleaner, more declarative)
✅ Refactor to explicit InMemoryRepo class (ready for multiple repo types)
✅ Complete FileRepo with JSON persistence and comprehensive tests
✅ TodoRepository Protocol for type-safe repo interfaces
✅ Protocol compliance verification with clean type checking
✅ Cleaned up old module-level repo code
✅ TodoCore and CLI dependency injection refactoring
✅ Write to a default file that is in a gitignored folder (.data/todos.json)
✅ Organized repo implementations into separate files (repo/ subfolder)
✅ SQLiteRepo implementation with database schema and ACID transactions
✅ Comprehensive SQLiteRepo test suite with Protocol compliance
✅ CLI switched to SQLiteRepo as default (.data/todos.db)
✅ Feature branch workflow with TCR methodology

## Parking Lot
- Ideas and questions that come up during development
- Things to explore later
- Refactoring opportunities
- Architecture decisions to revisit
- Todos can have optional descriptions
- The models probably belong in the core (domain models in domain layer) - TRICKIER: circular imports make this complex

## Decisions
- Use pattern matching for CLI argument parsing (clean, declarative, easy to test with args list)
- SQLiteRepo as default persistence layer (production-grade database with ACID guarantees)
- Organized repo structure: `/repo` subfolder with separate files per implementation
- Protocol-based architecture enables seamless repository swapping

## Notes
- When running TCR script, narrate the red/green feedback for user visibility (format ✅/❌, type check ✅/❌, tests ✅/❌)

---

*"Keep focused on the next clear step while tracking distractions separately."*