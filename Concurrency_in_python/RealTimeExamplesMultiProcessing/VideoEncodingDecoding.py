from multiprocessing import Process, Pool
import cv2
import numpy as np

def process_frame(frame):
    # Apply a filter or transformation
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def frames_to_video(frame_list, output_path, fps):
    """
    Converts a list of frames into a video.

    :param frame_list: List of frames (NumPy arrays).
    :param output_path: Path to save the video file.
    :param fps: Frames per second for the video.
    """
    if not frame_list:
        print("The frame list is empty. Cannot create a video.")
        return

    # Get the dimensions of the first frame
    height, width= frame_list[0].shape
    size = (width, height)

    # Initialize the VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, size, isColor=False)

    # Write each frame to the video
    for frame in frame_list:
        video_writer.write(frame)

    # Release the VideoWriter
    video_writer.release()
    print(f"Video saved at {output_path}")

frames = []
results = []
def videoFrames(video_path):
    cap = cv2.VideoCapture(video_path)
    # frame_id = 0
    # processes = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

def make_video():
    global results
    with Pool(processes=16) as pool:
        results =  pool.map(process_frame, frames)

if __name__ == "__main__":
    videoFrames("Videos/dog.mp4")
    make_video()
    output_path = "Videos/output_video.mp4"
    fps = 30
    frames_to_video(results, output_path, fps)
    # print(len(results))
    # print(results[0].shape)

