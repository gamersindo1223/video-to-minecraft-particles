import os
import shutil
from time import sleep
main_path = os.getcwd() + "/../result"
def make_audiopacks():
    dirpath = os.getcwd() + "/audio-packs"
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
    os.makedirs(dirpath + "/assets/audio-particles/sounds")  # make sounds dir
    with open(dirpath + "/pack.mcmeta", "w") as file:
        file.write("""{\n\x20\x20"pack":\x20{\n\t\t"pack_format":\x206,\n\t\t"description":\x20"§eGive §eit §ea §eStar §6https://github.com/gamersindo1223/video-to-minecraft-particles"\n\x20\x20}\n}""")
    with open(dirpath + "/assets/audio-particles/sounds.json", "w") as file:
        file.write("""{\n\x20\x20"particles_audios":\x20{\n\t"sounds":\x20["audio_particles:custom_particles_bgm_music.ogg"]\n\x20\x20}\n}""")

def make_datapack():
    dirpath  = "/particles-datapack"
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
    os.makedirs(dirpath + "/data/minecraft/tags/functions")
    os.makedirs(dirpath + "/data/img/functions/src")
    with open(dirpath + "/data/minecraft/tags/functions/load.json", "w") as file:
        file.write("""{\n\t"values": ["img:load"]\n}""")
    with open(dirpath + "/data/minecraft/tags/functions/tick.json", "w") as file:
        file.write("""{\n\t"values": ["img:tick"]\n}""")
    file_contents = {
        'load.mcfunction': 'tellraw @a {"text":"Particles have been loaded [Video-To-Minecraft-Particles]","color":"yellow","clickEvent":{"action":"run_command","value":"/function img:start"},"hoverEvent":{"action":"show_text","contents":["Click me to start the command! [The command will start near world spawn]"]}}',
        'tick.mcfunction': 'Content for file 2',
        'start.mcfunction': 'function img:src/1'
    }

    for file_name, content in file_contents.items():
        file_path = os.path.join(dirpath + "/data/img/functions/", file_name)
        with open(file_path, 'w') as file:
            file.write(content)