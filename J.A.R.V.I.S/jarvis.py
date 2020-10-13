import pyttsx3


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
print(voices)



def speak(audio):
    pass
