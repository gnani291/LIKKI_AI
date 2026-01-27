import pyttsx3

def speak(text):
    try:
        engine = pyttsx3.init('sapi5')   # Reinitialize every time (fixes freeze)

        voices = engine.getProperty('voices')

        # Force Female Voice (Zira)
        for voice in voices:
            if "zira" in voice.name.lower():
                engine.setProperty('voice', voice.id)

        engine.setProperty('rate', 165)
        engine.setProperty('volume', 1.0)

        print("\nLIKKI:", text)

        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print("TTS ERROR:", e)







