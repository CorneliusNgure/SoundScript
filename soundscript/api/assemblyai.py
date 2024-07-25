import assemblyai as aai
from .api_secrets import ASSEMBLYAI_API_KEY
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

aai.settings.api_key = ASSEMBLYAI_API_KEY

transcriber = aai.Transcriber()

def transcribe_audio(audio_url):
    try:
        logger.debug("Starting transcription")
        config = aai.TranscriptionConfig(speaker_labels=True)
        transcript = transcriber.transcribe(audio_url, config)
        logger.debug("Transcription completed successfully")

        return {
            'text': transcript.text,
            'utterances': [{'speaker': u.speaker, 'text': u.text} for u in (transcript.utterances or [])]
        }
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        raise
