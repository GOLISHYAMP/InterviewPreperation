#In GUI programs, multithreading is used to ensure the UI 
# remains responsive while background tasks
#  (e.g., file uploads, computations) are running.

import threading
import tkinter as tk
import time

def long_task():
    time.sleep(5)  # Simulate a long task
    print("Task completed")

def start_task():
    thread = threading.Thread(target=long_task)
    thread.start()

root = tk.Tk()
button = tk.Button(root, text="Start Task", command=start_task)
button.pack()
root.mainloop()
