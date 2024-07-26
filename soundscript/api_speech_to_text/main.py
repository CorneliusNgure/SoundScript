import sys
from api_communication import *

"""
This script handles the transcription process for an audio file 
as a command-line argument. 

It performs the following tasks:
1. Uploads the audio file to AssemblyAI.
2. Saves the transcription result to a text file.

Usage:
    python script_name.py path_to_audio_file
"""

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)