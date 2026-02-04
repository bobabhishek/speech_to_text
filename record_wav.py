"""
record_wav.py
-------------
Records microphone audio and saves a PCM 16-bit WAV
that is guaranteed compatible with Azure Speech SDK.
"""

import sounddevice as sd
import soundfile as sf

FILENAME = "sample_audio.wav"
DURATION = 5          # seconds
SAMPLE_RATE = 16000   # Azure recommended
CHANNELS = 1          # Mono

print("🎤 Recording will start now. Speak clearly...")
print("Say: 'Hello, please call me tomorrow'")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="int16"
)

sd.wait()

sf.write(FILENAME, audio, SAMPLE_RATE, subtype="PCM_16")

print(f"Recording saved as {FILENAME}")
