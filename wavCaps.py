import eyed3
import os
import mutagen
from mutagen import FileType
from mutagen import wave
from mutagen.id3 import ID3Tags, TextFrame, TIT2, TPE1
from colorama import Fore, Back, init

init(autoreset=True)

def wavCapper (file_str):
    song = wave.WAVE(os.path.join("Tests/"+ file_str))
    tags = song.tags

 #   for t in tags:
    if 'TIT2' in tags:
        title = str(tags['TIT2']).upper()
    else:
        title = None
    if 'TPE1' in tags:
        artist = str(tags['TPE1']).upper()
    else:
        artist = None
                
            
    if title == None or artist == None:
        if title == None and artist == None:
            print(Back.RED + "Both Artist and Song Title are empty")
        elif title == None:
            if artist.isupper(): 
                print(Back.BLUE + artist, Back.BLUE +  "Already Upper Case and title is empty")
            else: 
                song['ARTIST']= mutagen.id3.TextFrame(encoding=3, text=[artist])
                song.save()
                print(Back.GREEN + artist, Back.GREEN + "Successfully Capped and title is empty")
        elif artist == None:
            if title.isupper(): 
                print(Back.BLUE + title, Back.BLUE +  "Already Upper Case and artist name is empty")
            else: 
                song['TITLE']= mutagen.id3.TextFrame(encoding=3, text=[title])
                song.save()
                print(Back.GREEN + title, Back.GREEN + "Successfully Capped and artist name is empty")    
    elif title.isupper() and artist.isupper():
        print(Back.BLUE + artist, Back.BLUE +  "-", Back.BLUE +  title, Back.BLUE + "is Already Upper Case")
    else:
        song['TITLE']= mutagen.id3.TextFrame(encoding=3, text=[title])
        song['ARTIST']= mutagen.id3.TextFrame(encoding=3, text=[artist])
        song.save()
        print(Back.GREEN + artist, Back.GREEN +  "-", Back.GREEN + title, Back.GREEN + "Successfully Capped")
        
    return