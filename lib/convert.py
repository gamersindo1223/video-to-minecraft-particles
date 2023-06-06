# Converts images into Minecraft particles mcfunction file.
# To use this, you would need python 3 and PIL.
# This tool is created by Red Cocoon. Please do not remove this line, please :'(
# Red Cocoon is the original author I jsut modified this
import cv2
import os
from PIL import Image
import os 
from moviepy.editor import *
from make_folders import make_audiopacks
from time import sleep
import shutil


def convert(array_images, total_frames):
    index_ylyl = 0
    output_path = os.getcwd() + "/../result"
    #if os.path.exists(output_path):
    #    shutil.rmtree(output_path)
    #os.mkdir(output_path)
        #frame_folder = sorted(next(os.walk(f"{os.getcwd()}//frames"), (None, None, []))[2], key=lambda x: int(x.split('.')[0]))
    print("Starting to convert frames")
    for current_image in array_images:
        index_ylyl = index_ylyl + 1
        command = "particle minecraft:dust {0} {1} {2} {3} ~{4} ~ ~{5} 0 0 0 0.001 1"
        # This will produce 4096 particles in one frame, 64*64 = 4096 particles x*y
        particle_resolution = (64,64)

        particle_density = int(8)
        #image = Image.open(os.getcwd() + f"/frames/{current_image}")
        image = Image.fromarray(current_image)
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
                if index_ylyl+1 < len(array_images):
                    particles.append(f"schedule function img:src/{index_ylyl+1} {1/total_frames}s")
                    if index_ylyl == 1:
                        particles.insert(0, "tag @s add player")
                elif index_ylyl+1 == len(array_images):
                    particles.append("tag @a remove player")
                else:
                    pass
                for line in particles:
                    file.write(line+"\n")
    print("Finished!")
                        