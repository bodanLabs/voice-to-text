# 🎙️ Voice to Text with Python

This project demonstrates how to convert **speech from a microphone into text** using Python and the `speech_recognition` library.

Perfect for building:
- 🔹 Voice Notes tools
- 🔹 Voice Commands for apps
- 🔹 Smart Assistants

---

## 🚀 Features

- 🎧 Listens to your microphone in real-time
- 📝 Converts voice to text using Google Web Speech API
- ⚠️ Handles background noise and recognition errors gracefully

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install SpeechRecognition pyaudio
```

> 🔧 If `pyaudio` fails to install:
>
> - **Windows**:
>   ```bash
>   pip install pipwin
>   pipwin install pyaudio
>   ```
> - **macOS**:
>   ```bash
>   brew install portaudio
>   pip install pyaudio
>   ```

---

## 🧠 How It Works

The script uses:
- `speech_recognition.Recognizer()` to interpret audio
- `recognize_google()` to convert audio to text using Google API

---

## 🧪 Usage

Run the script:

```bash
python voice_to_text.py
```

Then speak into your microphone. It will output your speech as text in real-time.

---

## 📁 File Structure

```
voice-to-text-python/
│
├── voice_to_text.py    # Main Python script
├── README.md           # Project documentation
```
