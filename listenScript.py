# pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
# pip install pipwin
# pipwin install pyaudio
#pip install SpeechRecognition
import speech_recognition as sr
# pip install PyAudio


def listenExternalSpeech():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audioOut = r.listen(source, 0, 5)

    try:
        print("Interpreting... ")
        audioquery = r.recognize_google(audioOut, key= None, language="en-uk")
        print(f"You said: {audioquery}")
    except Exception as e:
        print(f"Error is: {str(e)}")
        return ""
    
    audioquery = str(audioquery)
    return audioquery.lower()

# listenExternalSpeech()