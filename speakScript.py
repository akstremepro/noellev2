################################################
## Last Code Update: 03-03-2022
## By: Akshat Negi
################################################




#*******************************#
## Load all required packages
#*******************************#

# pip install pyttsx3
import pyttsx3

## Initialize voice engine instances for using speech regonition features
engine = pyttsx3.init('sapi5')



def speakOutLoud(textData):

    ## Set requried properties
    engine.setProperty('rate', 200) 
    engine.setProperty('volume',1.0) 
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    ## Start text analysis and speak it out
    print(f"Noelle: {textData}")
    engine.say(text = textData)
    engine.runAndWait()
    #print("\n")

# speakOutLoud("Hello akshat")