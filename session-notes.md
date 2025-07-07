# TCR Kata Session Notes

## Today's Session Summary

### Major Achievements
🎉 **COMPLETED MAIN GOAL**: Create a todo from the command line
- Built fully working CLI with `add` and `list` commands
- Implemented clean architecture with dependency injection
- Set up proper module structure

### Architecture Built
```
models.py     ← Todo class (shared domain model)
core/         ← Domain logic with dependency injection  
repo.py       ← Storage functions (currently no-op)
cli.py        ← Command line interface with typed commands
```

### Key Patterns Implemented
- **TCR Flow**: Every change was tiny and immediately tested
- **Dependency Injection**: `_add_todo(title, store)` with clean seams  
- **Type-Driven Development**: Used type checker to drive interface design
- **Clean Command Pattern**: `AddCommand`/`ListCommand` → `run()` → domain
- **Separation of Concerns**: Parsing vs execution vs storage

### Working CLI Commands
```bash
poetry run python -m tcr_todo.cli add "buy milk"    # Returns: buy milk
poetry run python -m tcr_todo.cli list              # Returns: []
```

### Technical Decisions Made
- Python 3.10+ (modern union syntax `|`)
- Poetry for dependency management
- Pattern matching (`match`/`case`) for command dispatch
- Strict typing with mypy
- Auto-formatting with ruff
- Dependency injection for testability

### TCR Learnings Captured
- Package needs `poetry install` before importing src/ modules
- Forward references need quotes: `Callable[["Todo"], None]`
- Circular imports solved by extracting shared models
- Type checker can drive development (union types → pattern matching)

### Current State
- ✅ Full CLI working (add/list commands)  
- ✅ Clean architecture with DI ready
- ✅ Type-safe command dispatch
- 🔄 Storage layer ready but not implemented (just no-op)

### Next Session Ready
- All infrastructure in place for persistence
- Clear next steps identified
- Clean separation allows easy storage implementation