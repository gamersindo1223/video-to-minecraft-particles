"""

video_path = "video.mp4"  # Replace with the actual path to the video file
video_clip = mpy.VideoFileClip(video_path)
for frame in video_clip.iter_frames():
    try:
        frames.append(frame)
    except FileNotFoundError:
        print("Video file not found.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", str(e))
        sys.exit(1)
"""
import cv2
from time import sleep
import os
import sys
from lib.convert import convert
frames = []
print("This program only support .mp4 extension! Put your video into the same direcotry as this Program Directory!\nAnd rename it into video.mp4")
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print("Getting Frames")
if not os.path.exists(f"{os.getcwd()}/video.mp4"):
    raise Exception("Could not find video.mp4 in the current Directory!")
video = cv2.VideoCapture('video.mp4')
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
for frame_number in range(total_frames):
    try:
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video.read()
        if not ret:
            print("Cant rea frames")
            break
        frames.append(str(frame))
    except FileNotFoundError:
        print("Video file not found.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", str(e))
        sys.exit(1)
print("Finished Extracting frames, Now converting into a MC Function")
convert(frames, int(video.get(cv2.CAP_PROP_FRAME_COUNT)))