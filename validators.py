# validators.py
import json


def extract_confidence(result):
    """
    Safely extracts confidence score from Azure Speech result.
    Works even if NBest is missing.
    """

    if not result.json:
        return None

    data = json.loads(result.json)

    # NBest appears only when output_format = Detailed
    if "NBest" in data and len(data["NBest"]) > 0:
        return data["NBest"][0].get("Confidence")

    return None


def validate_and_correct_transcript(text):
    """
    Basic transcript validation and correction.
    """

    if not text:
        return "Empty transcript"

    corrections = {
        " pls ": " please ",
        " u ": " you ",
        " r ": " are "
    }

    text = text.lower()

    for wrong, correct in corrections.items():
        text = text.replace(wrong, correct)

    return text.capitalize()
