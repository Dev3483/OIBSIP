import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from youtubesearchpython import VideosSearch


def initialize_engine():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    return engine


def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()


def greet_user(engine):
    current_hour = int(datetime.datetime.now().hour)
    if current_hour >= 0 and current_hour < 12:
        speak_text(engine, "Good morning, sir!")
    elif current_hour >= 12 and current_hour < 18:
        speak_text(engine, "Good afternoon, sir!")
    else:
        speak_text(engine, "Good evening, sir!")
    speak_text(engine, "How may I help you today?")


def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Say that again, please...")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "none"


def search_youtube(query):
    try:
        videos_search = VideosSearch(query, limit=1)
        results = videos_search.result()
        if results['result']:
            first_result = results['result'][0]
            url = first_result['link']
            print(f"Opening {first_result['title']} on YouTube")
            webbrowser.open(url)
        else:
            speak_text(engine, "No results found on YouTube.")
    except Exception as e:
        print(e)
        speak_text(engine, "An error occurred while searching YouTube.")


if __name__ == "__main__":
    engine = initialize_engine()
    while True:
        query = get_user_input()

        if 'hello' in query:
            greet_user(engine)

        if 'wikipedia' in query:
            speak_text(engine, 'Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=4)
                speak_text(engine, "According to Wikipedia")
                print(results)
                speak_text(engine, results)
            except wikipedia.exceptions.DisambiguationError as e:
                print(e.options)
                speak_text(
                    engine, "There are multiple results. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak_text(engine, "No result found for the query.")
            except Exception as e:
                print(e)
                speak_text(
                    engine, "An error occurred while searching Wikipedia.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak_text(
                engine, "Please tell me what you want to search on YouTube.")
            query = get_user_input()
            search_youtube(query)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            webbrowser.open("jiosaavn.com")

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak_text(engine, f"Sir, the time is {str_time}")

        elif 'stop' in query:
            speak_text(engine, "Goodbye, sir. Have a nice day.")
            break
        else:
            continue
