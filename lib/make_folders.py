import os
import shutil
import os
def make_resourcepack(function_name, resourcepack_location):
    if os.path.exists(resourcepack_location):
        shutil.rmtree(resourcepack_location)
    os.makedirs(resourcepack_location + "/assets/minecraft/sounds")  # make sounds dir
    with open(resourcepack_location + "/pack.mcmeta", "w") as file:
        file.write("""{\n\x20\x20"pack":\x20{\n\t\t"pack_format":\x206,\n\t\t"description":\x20"§eGive §eit §ea §eStar §6https://github.com/gamersindo1223/video-to-minecraft-particles"\n\x20\x20}\n}""")
    with open(resourcepack_location + f"/assets/minecraft/sounds.json", "w") as file:
        file.write('{\n\x20\x20"'+function_name+'_audio":\x20{\n\t"sounds":\x20['+function_name+'_audio.ogg"]\n\x20\x20}\n}')

def make_datapack(function_name, datapack_location):
    dirpath  = datapack_location
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
    os.makedirs(dirpath + "/data/minecraft/tags/functions")
    os.makedirs(dirpath + f"/data/{function_name}/functions/src")
    with open(dirpath + "/data/minecraft/tags/functions/load.json", "w") as file:
        file.write('{\n\t"values": ["'+f"{function_name}:load"+'"]\n}')
    with open(dirpath + "/data/minecraft/tags/functions/tick.json", "w") as file:
        file.write('{\n\t"values": ["'+f"{function_name}:tick"+'"]\n}')
    file_contents = {
        'load.mcfunction': 'tellraw @a {"text":"Particles have been loaded [Video-To-Minecraft-Particles]","color":"yellow","clickEvent":{"action":"run_command","value":"/function '+ function_name +':start"},"hoverEvent":{"action":"show_text","contents":["Click me to start the command! [The command will spawn the particles below you]"]}}',
        'tick.mcfunction': '',
        'start.mcfunction': f'function {function_name}:src/1'
    }

    for file_name, content in file_contents.items():
        file_path = os.path.join(dirpath + f"/data/{function_name}/functions/", file_name)
        with open(file_path, 'w') as file:
            file.write(content)