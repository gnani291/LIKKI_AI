import speech_recognition as sr


def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("YOU:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""

    except sr.RequestError:
        print("❌ Speech service error")
        return ""



