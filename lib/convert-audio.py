import os 
from moviepy.editor import *
from make_folders import make_audiopacks
from time import sleep
import shutil

def convert_audio():
    video_path = "../video.mp4"
    video_clip = VideoFileClip(video_path)
    has_audio = video_clip.audio is not None
    if has_audio:
        make_audiopacks()
        sleep(5)
        video_clip.audio.write_audiofile(f"{os.getcwd()}/audio-packs/assets/audio-particles/sounds/custom_particles_bgm_music.ogg", after=lambda: shutil.make_archive("audio_particles_resouce_pack", 'zip', f'../result/audio-packs'))
    else:
        pass
