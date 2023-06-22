# Converts images into Minecraft particles mcfunction file.
# To use this, you would need python 3 and PIL.
# This tool is created by Red Cocoon. Please do not remove this line, please :'(
# Red Cocoon is the original author I jut modified this
import os
from PIL import Image
from moviepy.editor import *
import shutil
from lib.make_folders import make_resourcepack
def convert(array_images, total_frames, function_name, particles_density, datapack_location):
    """
    array_images = array of frames
    total frames = like the name
    function_name = function name
    """
    index_ylyl = 0
    #output_path = f"{os.getcwd()}/particles-datapack/data/{function_name}/functions/src"
    print("Starting to convert frames")
    for current_image in array_images:
        index_ylyl = index_ylyl + 1
        command = "execute as @a[tag=player,limit=1] run particle minecraft:dust {0} {1} {2} {3} ~{4} ~ ~{5} 0 0 0 0.001 1"
        # This will produce 4096 particles in one frame, 64*64 = 4096 particles x*y
        particle_resolution = (64,64)
        particle_density = int(particles_density)
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
            #with open(output_path + f"/{index_ylyl}.mcfunction", "w") as file:
            with open(f"{datapack_location}/data/{function_name}/functions/src{index_ylyl}.mcfunction", "w") as file:
                if index_ylyl+1 < len(array_images):
                    particles.append(f"schedule function {function_name}:src/{index_ylyl+1} {1/total_frames}s")
                    if index_ylyl == 1:
                        particles.insert(0, "tag @s add player")
                elif index_ylyl == len(array_images):
                    particles.append("tag @a remove player")
                else:
                    pass
                for line in particles:
                    file.write(line+"\n")
    shutil.make_archive(datapack_location, 'zip', f'${os.getcwd()}/result/particles_datapack')
    print("Finished!")

def convert_audio(file_location, function_name, resourcepack_path):
    video_clip = VideoFileClip(file_location)
    has_audio = video_clip.audio is not None
    if has_audio:
        make_resourcepack(function_name, resourcepack_path)
        video_clip.audio.write_audiofile(f"{resourcepack_path}/assets/minecraft/sounds/{function_name}_audio.ogg", 
        after=lambda: shutil.make_archive(resourcepack_path, 'zip', f'${os.getcwd()}/result/${function_name}_audio'))
    else:
        pass