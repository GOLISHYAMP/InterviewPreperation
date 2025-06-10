# Multithreading is used to handle different game components like:

# Physics calculations
# Rendering graphics
# Playing sound effects

import threading
import time

def play_music():
    while True:
        print("Playing background music...")
        time.sleep(2)

def game_loop():
    for i in range(10):
        print(f"Game frame {i}")
        time.sleep(1)

music_thread = threading.Thread(target=play_music, daemon=True)  # this thread cannot run individually
music_thread.start()

game_loop()
