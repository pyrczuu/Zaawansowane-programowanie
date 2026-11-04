import sqlite3
import time

DB_PATH = "queue.db"
CHECK_INTERVAL = 5  # sekundy
JOB_DURATION = 30  # sekundy


def claim_job():
    with sqlite3.connect(DB_PATH, timeout=10.0) as conn:
        cursor = conn.cursor()
        cursor.execute("BEGIN IMMEDIATE")

        cursor.execute("""
            SELECT id, task FROM jobs 
            WHERE status = 'pending' 
            LIMIT 1
        """)
        row = cursor.fetchone()

        if not row:
            conn.commit()
            return None

        job_id, task_name = row

        cursor.execute("""
            UPDATE jobs 
            SET status = 'in_progress' 
            WHERE id = ?
        """, (job_id,))

        conn.commit()
        return job_id, task_name


def mark_job_done(job_id):
    with sqlite3.connect(DB_PATH, timeout=10.0) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE jobs 
            SET status = 'done' 
            WHERE id = ?
        """, (job_id,))
        conn.commit()


def process_job():
    try:
        job = claim_job()
    except sqlite3.OperationalError:
        return False

    if not job:
        return False

    job_id, task_name = job
    print(f"[CONSUMER] Pobrano pracę ID: {job_id} ({task_name}). Wykonywanie ({JOB_DURATION}s)...")

    time.sleep(JOB_DURATION)

    mark_job_done(job_id)
    print(f"[CONSUMER] Zakończono pracę ID: {job_id} -> STATUS: done")
    return True


def run_consumer():
    print("[CONSUMER] Konsument uruchomiony. Oczekiwanie na zadania...")
    while True:
        has_processed = process_job()
        if not has_processed:
            time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    run_consumer()
