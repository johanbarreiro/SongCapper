import eyed3
import os
import mutagen
from mutagen import FileType
from mutagen.flac import FLAC
from mutagen.id3 import ID3Tags, TextFrame, TIT2, TPE1
from colorama import Fore, Back, init

init(autoreset=True)

def flacCapper (file_str):
    song = FLAC(os.path.join("Tests/"+ file_str))
    tags = song.tags
   
    for t in tags:
        if t[0].upper() == "ARTIST":
            artist = t[1]
        if t[0].upper() == "TITLE":
            title = t[1]
            

    if not artist:
        artist = "<empty>"

    print(Fore.YELLOW + "Now Reading:", artist, "-", title, Fore.YELLOW + "This is a FLAC file")    
 

    if title.isupper() and artist.isupper():
        print(Back.BLUE + artist, Back.BLUE +  "-", Back.BLUE +  title, Back.BLUE + "is Already Upper Case")
    else:
        song['TITLE']=title.upper()
        song['ARTIST']=artist.upper()
        song.save()
        print(Back.GREEN + artist, Back.GREEN +  "-", Back.GREEN + title, Back.GREEN + "Successfully Capped")

    return