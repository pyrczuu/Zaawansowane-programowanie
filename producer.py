import sqlite3
import sys
import uuid

DB_PATH = "queue.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        conn.commit()


def add_jobs(count=1, task_description="Rozmowa telefoniczna"):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for i in range(count):
            job_id = str(uuid.uuid4())[:8]
            desc = f"{task_description} #{i + 1}" if count > 1 else task_description
            cursor.execute(
                "INSERT INTO jobs (id, task, status) VALUES (?, ?, ?)",
                (job_id, desc, "pending")
            )
        conn.commit()
    print(f"[PRODUCER] Dodano {count} zadań do bazy SQLite.")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    add_jobs(count)
