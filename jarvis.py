import pyttsx3
import datetime 
import speech_recognition as sr
import pyaudio 
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour<=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am alexa , please tell me how may i help you ")

def takecommand() :
    #it takes microphone input from the user 'and return string output 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recogning....")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said : {query}\n')

    except Exception as e:
        # print(e)
        print("say that again please")
        return "none"
    return query
def sendEmail(to , content ):
    server = smtplib.SMPT('smntp.gmail.com' , 587) 
    server.ehlo()
    server.startls()
    server.login('youremail@gmail.com' , 'your password')
    server.sendmail('yourmail@gmail.com' , to , content)


 

if __name__=="__main__":
    wishme()
    takecommand()
    while True:
    # if 1 :
        query = takecommand().lower()
        #logic for excecuting taskes based on quaries
        if 'wikipedia' in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'F:\music for alexa'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir , the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to harry' in quary:
            try :
                speak("what should i say")
                content = takecommand()
                to = "sparshjoshi4172@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e :
                print(e)
                speak("soory my friend harry bhai, i am not able to send this email")




