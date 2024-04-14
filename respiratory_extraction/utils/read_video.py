import cv2
import numpy as np


def read_video_bgr(path: str) -> np.array:
    """
    Read a video file in BGR format and return a numpy array of frames
    :param path: path to the video file
    :return: numpy array of frames
    """

    cap = cv2.VideoCapture(path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frames = []
    for _ in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)

    cap.release()

    return np.array(frames)


def read_video_gray(path: str) -> np.array:
    """
    Read a video file in grayscale format and return a numpy array of frames
    :param path: path to the video file
    :return: numpy array of frames
    """

    frames = read_video_bgr(path)
    frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) for frame in frames]

    return np.array(frames)
