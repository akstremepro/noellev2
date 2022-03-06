import pandas as pd
import pyttsx3
import speech_recognition as sr
import sys
from sys import platform
import os
import time
import webbrowser
import numpy as np
# pip install opencv-python
import cv2

# pip install pymediawiki
from mediawiki import MediaWiki
# import wikipedia
import datetime
# pip install PyQt5
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType

import searchMaster
from searchMaster import youtubeSearch
from searchMaster import wikiSearch
from searchMaster import googleSearch
from searchMaster import amazonSearch
from searchMaster import stackOverflowSearch


# pip install pyautogui
import pyautogui

from dictionaryCode import translate,takeCommand

## RUn one time code to generate req.py file after every modification in UI file
# pyrcc5 req.qrc -o req_rc.py


# Define audtio engine properties
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)

# Define window flags
flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

def speakAction(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speakAction("Good morning")
    elif hour>=12 and hour<18:
        speakAction("Good Afternoon")
    else:
        speakAction("Good night")

    speakAction("Hi I am Noelle. How can i help you today")


class noelle(QThread):
    def __init__(self):
        super(noelle, self).__init__()

    def run(self):
        self.noellefunc()

    def speechtotext(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.25)
            audioinput = r.listen(source,0,10)

        try:
            print("Interpreting...")
            audiotext = r.recognize_google(audioinput, language= 'en-in')
            print(audiotext)
        except Exception as e:
            return "None"

        audiotext = audiotext.lower()
        return audiotext

    def noellefunc(self):
        wish()
        while True:
            self.query = self.speechtotext()
            if self.query == "None":
                #speakAction("Please repeat")
                self.query = self.speechtotext()


            if 'goodbye' in self.query:
                speakAction("See ya later alligator")
                sys.exit()


            elif self.query.find('open google') !=-1:
                webbrowser.open('www.google.com')
                speakAction("opening google")


            elif self.query.find('search google') !=-1:
                speakAction("What do you want to search on google?")
                searchterm = self.speechtotext()
                if searchterm =='None':
                    searchterm = self.speechtotext()
                googleSearch(searchterm)
                speakAction("This is what i found on google... ")


            elif self.query.find('open youtube') !=-1:
                webbrowser.open("www.youtube.com")
                speakAction("opening youtube")


            elif self.query.find('search youtube') !=-1:
                speakAction("What do you want to search on youtube?")
                searchterm = self.speechtotext()
                if searchterm == 'None':
                    searchterm = self.speechtotext()
                youtubeSearch(searchterm)
                speakAction("This is what i found on youtube... ")


            elif self.query.find('open amazon') !=-1:
                webbrowser.open('www.amazon.com')
                speakAction("opening amazon")


            elif self.query.find('search amazon') !=-1:
                speakAction("What do you want to search on amazon?")
                searchterm = self.speechtotext()
                if searchterm =='None':
                    searchterm = self.speechtotext()
                amazonSearch(searchterm)
                speakAction("This is what i found on amazon... ")


            elif self.query.find('open stack overflow') !=-1:
                webbrowser.open('www.stackoverflow.com')
                speakAction("opening stackoverflow")


            elif self.query.find('search stack overflow') != -1 :
                speakAction("What do you want to search on stackoverflow?")
                searchterm = self.speechtotext()
                if searchterm =='None':
                    searchterm = self.speechtotext()
                stackOverflowSearch(searchterm)
                speakAction("This is what i found on stackoverflow... ")


            elif self.query.find('wikipedia') != -1:
                speakAction("Searching Wikipedia...")
                results = wikiSearch(self.query)
                speakAction(f'According to Wikipedia these are the results...{results}')


            elif self.query.find('dictionary') != -1:
                speakAction("What do you want to search from smart dictionary...")
                translate(takeCommand())


            elif self.query.find('screenshot') != -1:
                speakAction("Taking current screenshot...")
                myscreenshot = pyautogui.screenshot()
                image = cv2.cvtColor(np.array(myscreenshot),  cv2.COLOR_RGB2BGR)
                cv2.imwrite(os.path.join(os.path.dirname(__file__),"./screenshot.png"), image)


            elif self.query.find('add reminder') != -1:
                df = pd.DataFrame(columns=["timestamp", "reminder", "status"], index=[0])
                speakAction("Please speak valid reminder message to add in text format...")

                self.query = self.speechtotext()
                print(self.query)
                ts = str(time.strftime("%A, %d %B %Y"))
                remindermessage = self.query
                df['timestamp'][0] = ts
                df['reminder'][0] = remindermessage
                df['status'][0] = "incomplete"
                print(remindermessage,"\n",ts)
                print(df)
                df1 = pd.read_csv("reminderDoc.csv", sep =',')
                df1 = pd.concat([df1, df])
                try:
                    df1.to_csv("reminderDoc.csv",sep=',', index=False, header= True)
                except Exception as e:
                    print (e)


            elif (self.query.find('edit reminder status') != -1) or (self.query.find('modify reminder status') != -1):
                df = pd.DataFrame(columns=["timestamp", "reminder", "status"], index=[0])
                speakAction("Please speak valid reminder message to add in text format...")

                self.query = self.speechtotext()
                print(self.query)
                ts = str(time.strftime("%A, %d %B %Y"))
                remindermessage = self.query
                df['timestamp'][0] = ts
                df['reminder'][0] = remindermessage
                df['status'][0] = "incomplete"
                print(remindermessage,"\n",ts)
                print(df)
                df1 = pd.read_csv("reminderDoc.csv", sep =',')
                df1 = pd.concat([df1, df])
                try:
                    df1.to_csv("reminderDoc.csv",sep=',', index=False, header= True)
                except Exception as e:
                    print (e)


            elif 'play music' in self.query:
                speakAction("playing music from pc")
                self.music_dir = "./music"
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir, self.musics[0]))





class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])







FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./noelleqt5.ui"))
print(FROM_MAIN,_)

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)

        # To adjust widget size
        self.setFixedSize(1100,800)

        self.title = "Noelle Chatbot UI"

        #self.exit = QPushButton
        self.exit.setStyleSheet("border-image:url(./stockimages/exit.png);\n")
        self.exit.clicked.connect(self.close)
        self.setWindowFlags(flags)

        botspeak = noelle()
        botspeak.start()

        self.ts = time.strftime("%A, %d %B %Y")
        self.pn = platform
        #self.setGeometry(0, 0, 1100, 800)
        self.background.setPixmap(QPixmap("./stockimages/whitebackground.jpg"))

        self.clocktext.setText("<font size=12 color='blue'>"+self.ts+"</font>")
        self.clocktext.setFont(QFont(QFont('Arial',6, QFont.Bold)))

        self.platformtext.setText("<font size=12 color='red'>" + self.pn + "</font>")
        self.platformtext.setFont(QFont(QFont('Arial', 6, QFont.Bold)))


        ##Table view
        df = pd.read_csv("reminderDoc.csv", sep =',')
        df = df.rename(columns={'taskid': 'TaskID', 'timestamp': 'Date', 'reminder': 'Reminder'})
        dfInC = df[df.status == 'incomplete']
        dfC = df[df.status == 'complete']
        dfInC = dfInC.drop(['status'], axis=1)
        dfC = dfC.drop(['status'],  axis=1)

        datareq = dfInC.values.tolist()
        self.modeli = TableModel(dfInC)
        self.tableViewpending.setModel(self.modeli)

        self.modelc = TableModel(dfC)
        self.tableViewcompleted.setModel(self.modelc)

        self.horizontal_headeri = self.tableViewpending.horizontalHeader()
        self.vertical_headeri = self.tableViewpending.verticalHeader()

        self.horizontal_headeri.setSectionResizeMode( QHeaderView.ResizeToContents)
        self.vertical_headeri.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.horizontal_headerc = self.tableViewcompleted.horizontalHeader()
        self.vertical_headerc = self.tableViewcompleted.verticalHeader()

        self.horizontal_headerc.setSectionResizeMode( QHeaderView.ResizeToContents)
        self.vertical_headerc.setSectionResizeMode(QHeaderView.ResizeToContents)


app = QtWidgets.QApplication(sys.argv)

main = Main()
main.show()
exit(app.exec_())
