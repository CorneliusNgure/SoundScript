import requests
from .secret_key import ASSEMBLYAI_API_KEY
import time

"""
This module handles audio file uploads to AssemblyAI, transcription requests, and
retrieval of transcription results. 

Functions:
- upload(filename): Uploads an audio file and returns the URL for the uploaded audio.
- transcribe(audio_url): Requests transcription for the given audio URL and returns the transcript ID.
- poll(transcript_id): Polls AssemblyAI for the status of the transcription request.
- get_transcription_result_url(audio_url): Retrieves the transcription result by polling.
- save_transcript(audio_url, filename): Saves the transcription result to a text file.
- process_transcription(filename): Manages the full transcription process.
"""

# UPLOAD
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': ASSEMBLYAI_API_KEY}

def upload(filename):
    """
    Uploads an audio file to AssemblyAI and returns the URL for the uploaded audio.

    Args:
        filename (str): The path to the audio file to be uploaded.

    Returns:
        str: The URL for the uploaded audio file.
    """
     
    def read_file(filename, chunk_size=5242880):
        """
        Generator function to read the file in chunks.

        Args:
            filename (str): The path to the file to be read.
            chunk_size (int): The size of each chunk to be read.

        Yields:
            bytes: The file data in chunks.
        """
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url

# TRANSCRIBE

def transcribe(audio_url):
    """
    Requests transcription for the given audio URL and returns the transcript ID.

    Args:
        audio_url (str): The URL of the audio file to be transcribed.

    Returns:
        str: The ID of the transcription request.
    """
    transcript_request = { "audio_url": audio_url }
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    # print(response.json())

    transcript_id = transcript_response.json()['id']
    return transcript_id

# audio_url = upload(filename)
# transcript_id = transcribe(audio_url)
# get_transcription_result_url(audio_url)

# print(transcript_id)

# POLL - to wait for the transcription process to be completed API
def poll(transcript_id):
    """
    Polls AssemblyAI for the status of the transcription request.

    Args:
        transcript_id (str): The ID of the transcription request.

    Returns:
        dict: The response JSON containing the transcription status and result.
    """
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    # print(polling_response.json())
    return polling_response.json()

def get_transcription_result_url(audio_url):
    """
    Retrieves the transcription result by polling until completion.

    Args:
        audio_url (str): The URL of the audio file to be transcribed.

    Returns:
        tuple: A tuple containing the response JSON and an error message (if any).
    """
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        # if polling_response.json()['status'] == 'completed':
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
        
        print('Waiting for 30 seconds...')
        time.sleep(30)


# SAVE TRANSCRIPT
def save_transcript(audio_url, filename):
    """
    Saves the transcription result to a text file.

    Args:
        audio_url (str): The URL of the audio file that was transcribed.
        filename (str): The path where the transcript file will be saved.

    Prints:
        - 'Transcription saved!' if the transcript is successfully saved.
        - 'Error!!' followed by the error message if there was an error.
    """
    data, error = get_transcription_result_url(audio_url)

    if data:
        text_filename = filename + '.txt'
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print('Transcription saved!')
    elif error:
        print('Error!!', error)

# HANLDING THE FULL TRNSCRIPTION 
def process_transcription(filename):
    """
    Manages the full transcription process from uploading the file to saving the transcript.

    Args:
        filename (str): The path to the audio file to be processed.
    """
    audio_url = upload(filename)
    save_transcript(audio_url, filename)