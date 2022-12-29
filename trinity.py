import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import pywhatkit
import pyjokes
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is Trinity. Please tell me! How may I help you?")


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day = {1: 'Monday', 2: 'Tuesday',
           3: 'Wednesday', 4: 'Thursday',
           5: 'Friday', 6: 'Saturday',
           7: 'Sunday'}
    if day in Day.keys():
        day_of_the_week = Day[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in',)
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'yourpassword')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            print('I am fine. What about you?')
            speak('I am fine. What about you?')

        elif 'fine' in query or "good" in query:
            print("It's good to know that your fine..")
            speak("It's good to know that your fine..")

        elif 'play' in query:
            song = query.replace('play', '')
            print('playing ' + song)
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open youtube' in query:
            speak('Ok Lets go')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'news' in query:
            print('Lets go to TIMES OF INDIA...')
            speak('Lets go to Times Of India...')
            webbrowser.open("https://timesofindia.indiatimes.com/?from=mdr")

        elif 'camera' in query or 'take a photo' in query:
            ec.capture(0, "Camera ", "img.jpg")
            print('Clicked')
            speak('Clicked. You are looking awesome.')

        elif 'open spotify' in query:
            speak('Ok Lets go')
            webbrowser.open("spotify.com")

        elif 'day' in query or 'what is the day' in query:
            print(tellDay())
            tellDay()

        elif 'joke' in query or 'tell me a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'created' in query or 'why you are created' in query:
            print(
                'I dont really know but i think, To destroy humans hahahahahahahahahaha')
            speak(
                'I dont really know but i think, To destroy humans hahahahahahahahahaha')

        elif 'send email' in query:
            try:
                speak("Okay")
                content = takeCommand()
                speak("whom should i send?")
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'thank' in query or 'bye' in query or 'goodnight' in query:
            print('Goodbye')
            speak('Well! Goodbye sir, May you have a nice day..')
            exit()
