import os
import speech_recognition as sr
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime
from tts_output import speak   # IMPORT TTS MODULE

# Load env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

# Initialize Groq
client = Groq(api_key=GROQ_API_KEY)


# Voice Input Function
def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.6)
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print("YOU:", query)
        return query.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand voice")
        return ""

    except sr.RequestError:
        print("❌ Speech service error")
        return ""


# AI Brain
def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are Likki, a friendly helpful female AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print("AI ERROR:", e)
        return "Sorry, I am having trouble connecting to my brain."


# MAIN LOOP
def main():

    print("================================")
    print(" 🤖 LIKKI AI Assistant Started ")
    print("================================")

    speak("Hello Gnani. I am Likki. You can speak now.")

    while True:

        query = listen()

        if query == "":
            continue

        # TIME COMMAND
        if "time" in query:
            time_now = datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_now}")

        # EXIT COMMAND
        elif "exit" in query or "bye" in query or "stop" in query:
            speak("Goodbye Gnani. Have a nice day.")
            break

        # AI RESPONSE
        else:
            answer = ask_ai(query)

            if answer:
                speak(answer)
            else:
                speak("Sorry, I could not generate a response.")


# Run
if __name__ == "__main__":
    main()





