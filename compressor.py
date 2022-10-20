import sys
import moviepy
from moviepy.editor import *
from os import path
import subprocess as sp
from moviepy.config import get_setting
from moviepy.tools import subprocess_call


clip = 'test.mp4'
video = path.splitext(clip)
name_video = video[0] + '_new.mp4'
print(name_video)



def compressor(clip):
    try:
        clip = VideoFileClip(clip)

    except FileNotFoundError as error:
        print("File not found ")

    clip = clip.resize ((1920,1080))
    clip.write_videofile(name_video, codec = 'libx264',audio_bitrate = '50k', preset = 'veryslow')


clip = compressor(clip)
    

