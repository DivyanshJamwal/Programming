import speech_recognition as sr
import pyttsx3
import os

speech = sr.Recognizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver fails to initialize')

voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
engine.setProperty('voice','default')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network error')
    return voice_text

if __name__ == '__main__':
    speak_text_cmd('Hello sir.. This is JARVIS as your Artificial Intelligence')

    while True:

        voice_note = read_voice_cmd()
        print('cmd : {}'.format(voice_note))

        if 'Hello' in voice_note:
            speak_text_cmd('Hello Sir. How can i help you?')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\ {}'.format(voice_note.replace('Open','')))
            continue
        elif 'bye' in voice_note:
            speak_text_cmd('Bye sir. Happy to help you. Have a good day')
            exit()