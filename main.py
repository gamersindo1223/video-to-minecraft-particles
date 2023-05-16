import cv2
import time
import shutil
import os
import convert
dirpath = os.getcwd() + "/frames"
print("This program only support mp4! Put your video into the same direcotry as this Program!\nAnd rename it into video.mp4")
time.sleep(5)
if os.path.exists(dirpath):
    shutil.rmtree(dirpath)
os.mkdir(dirpath)

if not os.path.exists(f"{os.getcwd()}\\video.mp4"):
    print("t")
    raise Exception("Could not find video.mp4 in the current Directory!")

video = cv2.VideoCapture('./video.mp4')
frame_count = 0
while True:
    success, frame = video.read()
    if not success:
        print("Finished Converting Video frames into A JPG!, or something happened idk")
        break
    cv2.imwrite(os.path.join(dirpath, f'{frame_count}.jpg'), frame)
    frame_count += 1