import threading
import time

def log_writer():
    while True:
        print("Writing logs...")
        time.sleep(2)

def main_task():
    for i in range(5):
        print(f"Processing step {i}")
        time.sleep(1)

log_thread = threading.Thread(target=log_writer, daemon=True)
log_thread.start()

main_task()
