from speakScript import *
# from noelle_run import noelle
import time
import pandas as pd
# testing code

# engine.say("Hello World!")
# rate = engine.getProperty('rate')
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

# speakOutLoud("Hello Akshat")
import pandas as pd
import speech_recognition as sr

def speakAction(audio):
    engine.say(audio)
    engine.runAndWait()


def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audioinput = r.listen(source,0,3)

    try:
        print("Interpreting...")
        audiotext = r.recognize_google(audioinput, language= 'en-in')
        print(audiotext)
    except Exception as e:
        return "None"

    audiotext = audiotext.lower()
    return audiotext


df = pd.DataFrame(columns=["timestamp", "reminder", "status"], index=[0])
speakAction("Please speak...")

query = speechtotext()
if query == "None":
    # speakAction("Please repeat")
    query = speechtotext()

print(query)
ts = str(time.strftime("%A, %d %B %Y"))
print(ts)
remindermessage = query
print(remindermessage)
df['timestamp'][0] = ts
df['reminder'][0] = remindermessage
df['status'][0] = "incomplete"
print(df)
try:
    df.to_csv("reminderDoc.csv", mode='a', index=False, header= False)
except Exception as e:
    print (e)
