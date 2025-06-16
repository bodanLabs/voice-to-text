import speech_recognition as sr

def listen_and_convert():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Say something... (press Ctrl+C to quit)")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                print("📝 You said:", text)
            except sr.UnknownValueError:
                print("❌ Could not understand audio")
            except sr.RequestError as e:
                print(f"⚠️ Could not request results from Google Speech Recognition service; {e}")
            except KeyboardInterrupt:
                print("\n👋 Exiting.")
                break

if __name__ == "__main__":
    listen_and_convert()
