"""SQLite-based todo repository implementation."""

import sqlite3
from pathlib import Path
from tcr_todo.models import Todo


class SQLiteRepo:
    """SQLite-based todo repository."""

    def __init__(self, db_path: str) -> None:
        """Initialize with database path."""
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        """Initialize the database schema."""
        # Ensure directory exists
        db_file = Path(self.db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL
                )
            """)
            conn.commit()

    def store_todo(self, todo: Todo) -> None:
        """Store a todo item to database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO todos (title) VALUES (?)", (todo.title,))
            conn.commit()

    def retrieve_todos(self) -> list[Todo]:
        """Retrieve todos from database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("SELECT title FROM todos ORDER BY id")
            rows = cursor.fetchall()
            return [Todo(title=row[0]) for row in rows]
