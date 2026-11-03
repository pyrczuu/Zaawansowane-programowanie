import csv
import os
import sys
import uuid
from filelock import FileLock

FILE_PATH = "queue.csv"
LOCK_PATH = "queue.csv.lock"


def add_job(task_description="Rozmowa telefoniczna"):
    job_id = str(uuid.uuid4())[:8]
    status = "pending"

    lock = FileLock(LOCK_PATH)
    with lock:
        file_exists = os.path.exists(FILE_PATH)

        with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["id", "task", "status"])
            writer.writerow([job_id, task_description, status])

    print(f"[PRODUCER] Dodano pracę ID: {job_id} | Status: {status}")


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    for i in range(count):
        add_job(f"Rozmowa telefoniczna #{i + 1}")