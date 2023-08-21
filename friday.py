import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
url = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
webbrowser.register('chrome',None, webbrowser.BackgroundBrowser(url))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good evening!")        

    speak("I am listener, What would you like me to do ?")

def takecommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
   
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in') 
        speak(f"You said: {query}\n")
        return query

    except Exception as e:
        print(e)
        speak("again please")      


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abhishekquckit@gmail.com','Quick@123')
    server.sendmail('abhishekquckit@gmail.com', to, content)
    server.close()
    


if __name__ == "__main__":

    wishme()
    while True:
        query = takecommand().lower()
        # Logic for taking task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "absk1901mff@gmail.com" 
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry your email can not be sent due to some errors")



