**SongCapper - Audio Metadata Editor**

This tool is designed to streamline the process of editing metadata for audio files within a specified directory. It utilizes the Mutagen library to interact with audio file metadata.

**Purpose**
This program aims to enhance the readability of music libraries, particularly for DJs engaged in freeform and unplanned DJ sets. It facilitates easy identification of songs, regardless of how artists stylize their song titles

***Functionality***
The program identifies the file type of each audio file (mp3, m4a, aiff, flac, or wav) and calls a corresponding function to read and write the tags in all uppercase letters. If the tool encounters a non-supported file type, it will notify you of this limitation.

For optimal performance, ensure that the audio files have existing song titles and artist names in their metadata.

***Usage***
main.py: Contains the main program that orchestrates the process, calling various functions and iterating over the specified directory.

[filetype]Caps: Each file type has a dedicated function in this section, handling the conversion of tags to uppercase.

***Modules Needed***
eyed3, os, mutagen, colorama
