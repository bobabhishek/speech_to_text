"""
fix_wav.py
----------
Re-encodes any WAV file into Azure Speech compatible PCM WAV.
"""

import soundfile as sf

INPUT_WAV = "sample_audio.wav"
OUTPUT_WAV = "sample_audio_fixed.wav"

# Read audio (any format)
data, samplerate = sf.read(INPUT_WAV)

# Force PCM 16-bit WAV
sf.write(
    OUTPUT_WAV,
    data,
    samplerate,
    subtype="PCM_16"
)

print("✅ WAV file fixed and saved as:", OUTPUT_WAV)
print("Sample rate:", samplerate)
