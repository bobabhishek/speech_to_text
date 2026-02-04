# speech_utils.py
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION


def speech_to_text_from_audio_file(audio_file_path):
    speech_config = speechsdk.SpeechConfig(
        subscription=AZURE_SPEECH_KEY,
        region=AZURE_SPEECH_REGION
    )

    speech_config.speech_recognition_language = "en-US"

    # 🔴 IMPORTANT: Enable detailed output for confidence scores
    speech_config.output_format = speechsdk.OutputFormat.Detailed

    audio_config = speechsdk.AudioConfig(filename=audio_file_path)

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    return recognizer.recognize_once()
