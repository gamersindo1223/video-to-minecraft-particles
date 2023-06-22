from termcolor import colored
import os
from moviepy.editor import *
from lib.convert import convert, convert_audio
from lib.make_folders import make_datapack
datapack_location = f'{os.getcwd()}/particles-datapack'
resourcepack_location = f'{os.getcwd()}/audio-packs'
def main(frames, total_frames, question_answer, filelocation):
    os.system('cls' if os.name == 'nt' else 'clear')
    function_name = question_answer['function-name']
    make_datapack(function_name, datapack_location)
    convert(frames, total_frames, function_name, question_answer['particles-density'], datapack_location)
    convert_audio(filelocation, function_name, resourcepack_location)
    os.system('cls' if os.name == 'nt' else 'clear')
    