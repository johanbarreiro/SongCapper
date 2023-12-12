import mp3Capper
import m4aCapper
import flacCapper
import wavCapper
import aiffCapper
import os
from colorama import Fore

directory = "/Users/johanbarreiro/Documents/Coding/allCaps/Tests"

for filename in os.listdir(directory):
    if filename.endswith(".mp3"): 
        print("\n", os.path.join(directory, filename))
        mp3Capper(filename)
    elif filename.endswith(".wav"):
        print("\n", os.path.join(directory, filename))
        wavCapper(filename)
    elif filename.endswith(".flac"): 
        print("\n", os.path.join(directory, filename))
        flacCapper(filename)
    elif filename.endswith(".m4a"): 
        print("\n", os.path.join(directory, filename))
        m4aCapper(filename)
    elif filename.endswith(".aiff"): 
        print("\n", os.path.join(directory, filename))
        aiffCapper(filename)    
    else:
        print("\n", os.path.join(directory, filename))
        print(Fore.RED + "You Fool! This is not a valid file type!")