import eyed3
import os
import mutagen
from mutagen import FileType
from mutagen.id3 import ID3Tags, TextFrame, TIT2, TPE1
from colorama import Fore, Back, init



init(autoreset=True)

def mp3Capper(file_str):
    song = eyed3.core.load(os.path.join("Tests/"+ file_str))
    title = song.tag.title
    artist = song.tag.artist

    if not artist:
        #print("none is false")
        artist = "<empty>"

    print(Fore.YELLOW + "Now Reading:", artist, "-", title, Fore.YELLOW + "This is a mp3 file")
    print(song.tag)

    if title.isupper() and artist.isupper():
        print(Back.BLUE + artist, Back.BLUE +  "-", Back.BLUE +  title, Back.BLUE + "is Already Upper Case")
    else:
        song.tag.title = title.upper()
        song.tag.artist = artist.upper()
        song.tag.save()
        print(Back.GREEN + artist, Back.GREEN +  "-", Back.GREEN + title, Back.GREEN + "Successfully Capped")
    
    return