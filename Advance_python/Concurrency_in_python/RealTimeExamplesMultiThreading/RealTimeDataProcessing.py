#For example, reading data from a sensor or a video
#  feed while performing processing on a separate thread.

import threading
import cv2
import time

def func():
    count = 0
    while count < 20:
        print("hello")
        time.sleep(2)
        count += 1


def process_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Process frame
        cv2.imshow("Gray Frame", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

thread = threading.Thread(target=process_frames)
printthread = threading.Thread(target=func)
thread.start()
printthread.start()
thread.join()
printthread.join()