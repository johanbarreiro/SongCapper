import mp3Caps
import m4aCaps
import flacCaps
import wavCaps
import aiffCaps
import os
from colorama import Fore

directory = "INSERT DIRECTORY HERE"

for filename in os.listdir(directory):
    if filename.endswith(".mp3"): 
        print("\n", os.path.join(directory, filename))
        mp3Caps.mp3Capper(filename)
    elif filename.endswith(".wav"):
        print("\n", os.path.join(directory, filename))
        wavCaps.wavCapper(filename)
    elif filename.endswith(".flac"): 
        print("\n", os.path.join(directory, filename))
        flacCaps.flacCapper(filename)
    elif filename.endswith(".m4a"): 
        print("\n", os.path.join(directory, filename))
        m4aCaps.m4aCapper(filename)
    elif filename.endswith(".aiff"): 
        print("\n", os.path.join(directory, filename))
        aiffCaps.aiffCapper(filename)    
    else:
        print("\n", os.path.join(directory, filename))
        print(Fore.RED + "You Fool! This is not a valid file type!")