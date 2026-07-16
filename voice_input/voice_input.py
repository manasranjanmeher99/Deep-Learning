import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening= sr.Recognizer()
engine= pt.init()  # fixed


def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd=""
    try:
        with sr.Microphone() as mic:
            print("Listening....")
            voice= listening.listen(mic)
            cmd= listening.recognize_google(voice)
            cmd= cmd.lower()

            if "ranjan" in cmd:
                cmd= cmd.replace("ranjan", "")
                print(cmd)
    
    except Exception as e:
        print("Error: ",e)

    return cmd

def run():
    cmd= hear()

    if "play" in cmd:
        song= cmd.replace("play","")
        speak("playing" + song)
        pk.playonyt(song)

run()