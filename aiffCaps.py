import eyed3
import os
import mutagen
from mutagen import FileType
from mutagen.aiff import AIFF
from mutagen.id3 import ID3Tags, TextFrame, TIT2, TPE1
from colorama import Fore, Back, init

init(autoreset=True)

def aiffCapper (file_str):
    song = AIFF(os.path.join("Tests/"+ file_str))
    tags = song.tags
    title = tags.getall('TIT2')[0].text[0]
    artist = tags.getall('TPE1')[0].text[0]
    
    print(Fore.YELLOW + file_str, Fore.YELLOW + "this is an aiff file")

    if title.isupper() and artist.isupper():
        print(Back.BLUE + artist, Back.BLUE +  "-", Back.BLUE +  title, Back.BLUE + "is Already Upper Case")
    else:
        tags.setall('TIT2',[TIT2(3,title.upper())])
        tags.setall('TPE1',[TPE1(3,artist.upper())])
        tags.save()
        print(Back.GREEN + artist, Back.GREEN +  "-", Back.GREEN + title, Back.GREEN + "Successfully Capped")
    return