# Converts images into Minecraft particles mcfunction file.
# To use this, you would need python 3 and PIL.
# This tool is created by Red Cocoon. Please do not remove this line, please :'(
# Red Cocoon is the original author I jsut modified this
import cv2
import os
from time import sleep
from PIL import Image
import shutil
index_ylyl = int(0)
directory = os.getcwd() + "/mdkir"
need_check_fps = True
video = cv2.VideoCapture('./video.mp4')
"""
while need_check_fps:
    print( len(os.listdir('./frames')))
    sleep(4)
   
    if int(video.get(cv2.CAP_PROP_FRAME_COUNT)) != len(os.listdir('path')):
        e
    print("Frames in directory is not the same as the video frames\nCheck ", )
"""
is_true = True
while is_true :
    if int(video.get(cv2.CAP_PROP_FRAME_COUNT)) != len(os.listdir('./frames')):
        sleep(2.5)
    elif int(video.get(cv2.CAP_PROP_FRAME_COUNT)) == len(os.listdir('./frames')):
            is_true = False
            if os.path.exists(os.getcwd() + "/result"):
                shutil.rmtree(os.getcwd() + "/result")
            os.mkdir(os.getcwd() + "/result")
            frame_folder = sorted(next(os.walk(f"{os.getcwd()}//frames"), (None, None, []))[2], key=lambda x: int(x.split('.')[0]))
            print(frame_folder )
            for current_image in frame_folder:
                index_ylyl = index_ylyl + 1
                command = "particle minecraft:dust {0} {1} {2} {3} ~{4} ~ ~{5} 0 0 0 0.001 1"
                output_path = os.getcwd() + "/result"
                particle_resolution = (64,64)
                particle_density = int(8)
                image = Image.open(os.getcwd() + f"/frames/{current_image}")
                image.thumbnail(particle_resolution)
                img_x, img_y = image.size
                rgba_img = image.convert('RGBA')
                def normalize_color(color):
                    new_color = []
                    for i in range(4):
                        new_color.append(color[i]/255)
                    return new_color
                particles = []
                for i in range(img_x):
                    for j in range(img_y):
                        color = normalize_color(rgba_img.getpixel((i, j)))
                        relative_x = float((img_x/2)-i)/particle_density
                        relative_y = float((img_y/2)-j)/particle_density
                        new_command = command.format(color[0],color[1],color[2],color[3],relative_x,relative_y)
                        particles.append(new_command)
                with open(output_path + f"/{index_ylyl}.mcfunction", "w") as file:
                    if index_ylyl+1 < len(frame_folder):
                        particles.append(f"function img:src/{index_ylyl+1}")
                    for line in particles:
                        file.write(line+"\n")