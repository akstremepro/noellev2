from urllib.request import urlopen
import urllib.parse
import webbrowser
from mediawiki import MediaWiki

def googleSearch(searchterm):
    url = 'https://google.com/search?q=' + searchterm
    print(url)
    webbrowser.open(url)


def youtubeSearch(searchterm):
    url  = "https://www.youtube.com/results?search_query=" + searchterm
    print(url)
    webbrowser.open(url)


def amazonSearch(searchterm):
    s1 = searchterm.replace(' ','-')
    s2 = searchterm.replace(' ','+')
    url = 'https://www.amazon.com/'+s1+'/s?k=' + s2
    print(url)
    webbrowser.open(url)


def stackOverflowSearch(searchterm):
    searchterm = searchterm.replace(' ','+')
    url = 'https://stackoverflow.com/search?q=' + searchterm
    print(url)
    webbrowser.open(url)


def wikiSearch(query):
    try:
        query = query.replace('wikipedia', '')
        query = query.replace(' ', '_')
        query = query.capitalize()
        wikipedia = MediaWiki()
        results = wikipedia.summary(query, sentences=5)
        print(results)
        return results
    except Exception as e:
        print(e)
        return 'None'

