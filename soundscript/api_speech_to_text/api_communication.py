import requests
from .secret_key import ASSEMBLYAI_API_KEY
import time

# UPLOAD
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': ASSEMBLYAI_API_KEY}

def upload(filename):
    def read_file(filename, chunk_size=5242880):
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
    transcript_request = { "audio_url": audio_url } #data being sent to AssemblyAI
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
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    # print(polling_response.json())
    return polling_response.json()

def get_transcription_result_url(audio_url):
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
    data, error = get_transcription_result_url(audio_url)

    if data:
        text_filename = filename + '.txt'
        with open(text_filename, 'w') as f:
            f.write(data['text'])
        print('Transcription saved!')
    elif error:
        print('Error!!', error)

# HANLDING THE FULL TRNSCRIPTION PROCESS
def process_transcription(filename):
    audio_url = upload(filename)
    save_transcript(audio_url, filename)