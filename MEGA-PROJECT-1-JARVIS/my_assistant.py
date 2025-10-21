import speech_recognition as sr
import pyttsx3
import webbrowser

# -----------------------------
# Initialize speech engines
# -----------------------------
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')  # Windows ke liye
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice
engine.setProperty('rate', 170)  # speaking speed

# -----------------------------
# Speak Function
# -----------------------------
def speak(text):
    """Speaks the given text"""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# -----------------------------
# Process Commands Function
# -----------------------------
def processCommand(command):
    """Performs action based on voice command"""
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")

    elif "stop" in command or "exit" in command:
        speak("Goodbye Komal!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":
    speak("Initializing with Komal...")

    while True:
        try:
            # Step 1: Listen for the wake word “Komal”
            with sr.Microphone() as source:
                print("\nListening for wake word 'Komal'...")
                r.pause_threshold = 1
                audio = r.listen(source)

            word = r.recognize_google(audio, language="en-in").lower()
            print(f"You said: {word}")

            # Step 2: If wake word detected
            if "komal" in word:
                speak("Ha boliye")   # 🔊 Voice output
                print("Ha boliye...")

                # Step 3: Listen for next command
                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = r.listen(source)

                command = r.recognize_google(audio, language="en-in")
                print(f"Command: {command}")

                # Step 4: Process the command
                processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn’t understand that.")
        except sr.RequestError as e:
            print(f"Speech service error: {e}")
