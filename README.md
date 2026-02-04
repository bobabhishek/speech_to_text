# Speech-to-Text Utility using Azure Speech Services

## 📌 Project Overview

This project implements a **Speech-to-Text (STT) utility** using **Azure Cognitive Services – Speech API**.  
It converts spoken audio (WAV format) into text, extracts **confidence scores**, and performs **basic transcript validation and correction**.

The project is designed using a **modular architecture**, following real-world software engineering best practices for clarity, scalability, and maintainability.

---

## 🎯 Objectives

- Convert speech audio into text using Azure Speech API
- Support audio file input (multi-modal input)
- Handle API reliability using retry logic
- Extract and interpret confidence scores
- Validate and correct speech transcripts
- Demonstrate clean, modular Python design

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Cloud Service:** Azure Cognitive Services – Speech  
- **Libraries:**
  - `azure-cognitiveservices-speech`
  - `python-dotenv`
  - `sounddevice`
  - `soundfile`

---

## 📁 Project Structure

speech_to_text/
│
├── .env
├── config.py
├── speech_utils.py
├── validators.py
├── retry.py
│
├── record_wav.py
├── fix_wav.py
│
├── test_audio_input.py
├── main_test_runner.py
│
└── sample_audio.wav


---

## 📂 File Descriptions

### `config.py`
- Loads Azure Speech API key and region from environment variables
- Prevents hardcoding of credentials
- Centralized configuration management

---

### `speech_utils.py`
- Core module for interacting with Azure Speech SDK
- Configures speech recognition settings
- Enables **detailed output format** for confidence scores
- Handles speech-to-text conversion from audio files

---

### `retry.py`
- Implements retry logic for handling temporary API or network failures
- Improves reliability of Azure Speech API calls

---

### `validators.py`
- Extracts confidence scores safely from Azure Speech response
- Performs transcript validation and basic text correction
- Handles edge cases where confidence data may be unavailable

---

### `record_wav.py`
- Records microphone input using Python
- Generates a **PCM 16-bit WAV file** compatible with Azure Speech API
- Ensures correct audio format for reliable recognition

---

### `fix_wav.py`
- Utility script used to re-encode invalid WAV files into PCM format
- Helpful during debugging and audio preprocessing

---

### `test_audio_input.py`
- Integration layer that combines:
  - Speech recognition
  - Retry logic
  - Confidence extraction
  - Transcript validation
- Handles recognized, no-match, and error scenarios

---

### `main_test_runner.py`
- Single entry point to execute the application
- Calls the test pipeline internally
- Designed for easy evaluation and execution

---

## ▶️ How to Run the Project

### Step 1: Install dependencies
```bash
pip install azure-cognitiveservices-speech python-dotenv sounddevice soundfile



