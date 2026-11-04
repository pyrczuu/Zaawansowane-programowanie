import csv
import os
import time
from filelock import FileLock

FILE_PATH = "queue.csv"
LOCK_PATH = "queue.csv.lock"
CHECK_INTERVAL = 5  # sekundy
JOB_DURATION = 30   # sekundy


def process_job():
    lock = FileLock(LOCK_PATH)
    job_to_do = None
    rows = []

    with lock:
        if not os.path.exists(FILE_PATH):
            return False

        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        if not reader:
            return False

        header = reader[0]
        data = reader[1:]

        for row in data:
            if len(row) == 3 and row[2] == "pending" and job_to_do is None:
                row[2] = "in_progress"
                job_to_do = row
            rows.append(row)

        if job_to_do:
            with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerows(rows)

    if not job_to_do:
        return False

    job_id, task_name, _ = job_to_do
    print(f"[CONSUMER] Pobrano pracę ID: {job_id} ({task_name})."
          f" Wykonywanie ({JOB_DURATION}s)...")

    time.sleep(JOB_DURATION)

    with lock:
        rows = []
        with open(FILE_PATH, mode="r", newline="", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        header = reader[0]
        data = reader[1:]

        for row in data:
            if len(row) == 3 and row[0] == job_id:
                row[2] = "done"
            rows.append(row)

        with open(FILE_PATH, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(rows)

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
