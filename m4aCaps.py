import eyed3
import os
import mutagen
from mutagen import FileType
from mutagen.mp4 import MP4
from mutagen.id3 import ID3Tags, TextFrame, TIT2, TPE1
from colorama import Fore, Back, init

init(autoreset=True)

def m4aCapper (file_str):
    song = MP4(os.path.join("Tests/"+ file_str))
    tags = song.tags 
    title = tags["\xa9nam"][0]
    artist = tags["\xa9ART"][0]

    if not artist:
        #print("none is false")
        artist = "<empty>"

    print(Fore.YELLOW + "Now Reading:", artist, "-", title, Fore.YELLOW + "This is a m4a file")    
 

    if title.isupper() and artist.isupper():
        print(Back.BLUE + artist, Back.BLUE +  "-", Back.BLUE +  title, Back.BLUE + "is Already Upper Case")
    else:
        tags["\xa9nam"]= title.upper()
        tags["\xa9ART"] = artist.upper()
        song.save()
        print(Back.GREEN + artist, Back.GREEN +  "-", Back.GREEN + title, Back.GREEN + "Successfully Capped")


    return