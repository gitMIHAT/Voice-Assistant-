import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print("Processing command:", c)
    if "open google" in c.lower():
        speak("Opening Google, Captain")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube, Captain")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook, Captain")
        webbrowser.open("https://www.facebook.com")
    else:
        speak("Sorry Captain, I didn’t understand that.")

if __name__ == "__main__":
    speak("Initializing... This is Ghost")
    try:
        while True:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                try:
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    word = recognizer.recognize_google(audio)
                    print("Heard:", word)

                    # Wake word detection
                    if "ghost" in word.lower():
                        speak("Yes Captain!")

                        # Now listen for the actual command
                        with sr.Microphone() as cmd_source:
                            speak("Ghost Activated")
                            print("Ghost activated, waiting for command...")
                            recognizer.adjust_for_ambient_noise(cmd_source, duration=0.5)
                            command_audio = recognizer.listen(cmd_source, timeout=10)
                            command = recognizer.recognize_google(command_audio)
                            print("Command:", command)
                            processCommand(command)

                except sr.UnknownValueError:
                    # Just ignore noise/silence
                    continue
                except sr.WaitTimeoutError:
                    # Timeout → just restart listening
                    continue
                except sr.RequestError as e:
                    print("Speech recognition error:", e)
                except Exception as e:
                    print("Error:", e)

    except KeyboardInterrupt:
        print("\n[System] Ghost shutting down. Goodbye Captain.")
        speak("Shutting down. Goodbye Captain.")
