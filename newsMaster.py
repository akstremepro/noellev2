import requests
import json
import pyttsx3
import speech_recognition as sr

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


def speak_news():
    try:
        url = 'https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=6e3f0bf5f4564424bade89d9cb8cd46e'
        news = requests.get(url).text
        news_dict = json.loads(news)
        articlelist = news_dict['articles']
        speak('General Category News')
        speak('Top Headlines from India are...')
        print(articlelist,"\n",news_dict)
        for index, articles in enumerate(articlelist):
            speak(articles['title'])
            if index == len(articlelist)-1:
                break

            if index%5 == 0:
                speak("Do you want to quit reading headlines? Say Yes or No")
                ans = takeCommand().lower()
                print(ans)
                if 'yes' in ans:
                    speak('End of reading headlines..')
                    break
                elif 'no' in ans:
                    speak('These were the top headlines, Have a nice day...')
                    continue

            speak('Moving on the next news headline...')
        speak('These were the top headlines, Have a nice day...')
    except Exception as e:
        print(e)

def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=uk&category=general&apiKey=6e3f0bf5f4564424bade89d9cb8cd46e'

if __name__ == '__main__':
    speak_news()