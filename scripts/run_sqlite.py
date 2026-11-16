import sqlite3, sys
from pathlib import Path
if len(sys.argv)<2: raise SystemExit("Usage: python scripts/run_sqlite.py path/to/script.sql")
sql=Path(sys.argv[1]).read_text(encoding="utf-8")
con=sqlite3.connect(":memory:")
con.executescript(sql)
print("SQL executed successfully in an in-memory SQLite database.")
print("Tables:", [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")])
con.close()
