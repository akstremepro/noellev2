from difflib import get_close_matches
import pyttsx3
import json
import speech_recognition as sr

# Load dictionary data
dictionarydata = json.load(open('dictionarydata.json'))

# Load engine for STT
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 490
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Interpreting...')
        query = r.recognize_google(audio, language='en-uk')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Please repeat...')
        return 'None'
    return query


def translate(word):
    word = word.lower()
    if word in dictionarydata:
        speak(dictionarydata[word])
    elif len(get_close_matches(word, dictionarydata.keys())) > 0:
        x = get_close_matches(word, dictionarydata.keys())[0]
        speak('Did you mean ' + x +
              ' instead,  respond with Yes or No.')
        ans = takeCommand().lower()
        if 'yes' in ans:
            speak(dictionarydata[x])
        elif 'no' in ans:
            speak("Word doesn't exist. Please ensure you spelled it correctly.")
        else:
            speak("I did not understand your entry.")

    else:
        speak("Word doesn't exist. Please double check it.")


if __name__ == '__main__':
    translate()