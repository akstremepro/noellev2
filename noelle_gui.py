################################################
## Last Code Update: 03-03-2022
## By: Akshat Negi
################################################

#*******************************#
## Load all required packages
#*******************************#

# pip install SpeechRecognition
import speech_recognition as sr
# pip install playsound
import playsound
# pip install pyttsx3
import pyttsx3
import time
from time import ctime
# pip install wikipedia
import wikipedia
import datetime
import os
import random
import webbrowser
import sys
from sys import platform as ptf
from gtts import gTTS
from listenScript import listenExternalSpeech as LES
from speakScript import speakOutLoud as SOL
from tkinter import *
# pip install Pillow
from PIL import ImageTk, Image


print('Listening...')
r = sr.Recognizer()
speaker = pyttsx3.init()


def record_audio(ask=False):
    # user voice record

    with sr.Microphone() as source:
        if ask:
            lee_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('Recognizer voice :' + voice_data)

        except Exception:
            print('Oops something went Wrong')
            # lee_voice('Oops something went Wrong')
        return voice_data


def lee_voice(audio_string):
    # Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

class Widget:
    def __init__(self):
        root = Tk()
        root.title('Noelle')
        root.geometry('640x480')

        img = ImageTk.PhotoImage(Image.open("noelleImage.png"))
        mainpanel = Label(root, image= img)
        mainpanel.pack(side = 'right', fill='both', expand = 'no')

        ## Initialize human and bot communication strings
        bottext = StringVar()
        humantext = StringVar()

        humantext.set("Your Personal Digital Assistant")
        humanFrame = LabelFrame(root, text = 'Noelle', font = ('Arial',28, 'bold'))

        humanFrame.pack(fill='both', expand='yes')

        top = Message(humanFrame, textvariable=humantext, bg='black', fg='white')
        top.config(font=("Century Gothic", 18, 'bold'))
        top.pack(side='top', fill='both', expand='yes')

        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),
                     bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy)\
            .pack(fill='x', expand='no')
        lee_voice('How can i help you?')
        root.mainloop()
        
    def clicked(self):
        # BUTTON CALLING
        print("working...")

        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'who are you' in voice_data:
            lee_voice('My name is Lena ')
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            lee_voice('Here is what i found' + search)

        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            lee_voice('Here is location' + location)

        if 'what is the time' in voice_data:
            lee_voice("Sir the time is :" + ctime())

        if 'exit' in voice_data:
            lee_voice('Thanks have a good day ')
            exit()


if __name__== '__main__':
    widget = Widget()

time.sleep(1)
while 1:
    voice_data = record_audio()
    #respond(voice_data)

speaker.runAndWait()
