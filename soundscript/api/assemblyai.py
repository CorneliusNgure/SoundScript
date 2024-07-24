import assemblyai as aai
from .api_secrets import ASSEMBLYAI_API_KEY

aai.settings.api_key = ASSEMBLYAI_API_KEY

transcriber = aai.Transcriber()

def transcribe_audio(audio_url):
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcript = transcriber.transcribe(audio_url, config)
    return {
        'text': transcript.text,
        'utterances': [{'speaker': u.speaker, 'text': u.text} for u in transcript.utterances]
    }
