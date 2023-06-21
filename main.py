import tkinter as tk
import tkinter.filedialog
import cv2
import os
from lib.main import main
import inquirer, re  
from termcolor import colored

#ask vid location
filetypes = (('MP4 files', '*.MP4'),)
root = tk.Tk()
filelocation = tk.filedialog.askopenfilename(title='Select a video file to convert',filetypes=filetypes)
root.destroy()
if(filelocation == ""):
    raise Exception("No video file")
print(filelocation)
questions = [inquirer.Text('function-name', message="What is the function name?",validate=lambda _, x: re.match('[A-Za-z]', x), default="particles")]
inqanswers = inquirer.prompt(questions)
# convert frames
frames = []
os.system('cls' if os.name == 'nt' else 'clear')
print("Getting Frames")
video = cv2.VideoCapture(filelocation)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
for frame_number in range(total_frames):
    try:
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = video.read()
        if not ret:
            raise Exception("Can't read frames")
        frames.append(str(frame))
    except Exception as e:
        raise Exception("An error occurred:", str(e))
print("Finished Extracting frames, Now converting into a MC Function")
main(frames, int(video.get(cv2.CAP_PROP_FRAME_COUNT)), inqanswers)