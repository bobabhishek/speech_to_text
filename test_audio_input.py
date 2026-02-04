# test_audio_input.py
from speech_utils import speech_to_text_from_audio_file
from validators import extract_confidence, validate_and_correct_transcript
from retry import retry_operation
import azure.cognitiveservices.speech as speechsdk


def run_audio_test(audio_file):
    result = retry_operation(
        lambda: speech_to_text_from_audio_file(audio_file)
    )

    print("\n--- AZURE RESULT DEBUG ---")
    print("Reason:", result.reason)

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        confidence = extract_confidence(result)
        corrected = validate_and_correct_transcript(result.text)

        print("\n--- TEST OUTPUT ---")
        print("Raw Transcript:", result.text)
        print("Corrected Transcript:", corrected)
        print("Confidence Score:", confidence)

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("❌ No recognizable speech found.")
        print("👉 Tip: Speak louder and avoid silence at the beginning.")

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation = result.cancellation_details
        print("❌ Recognition canceled:", cancellation.reason)
        print("Details:", cancellation.error_details)
