import pyttsx3
import speech_recognition as sr
import datetime as dt
import cv2
import subprocess
import os

engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=dt.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def note():
    speak("opening notepad")
    os.system(command="start notepad.exe")
def wordpad():
    speak("opening wordpad")
    os.system(command="start wordpad.exe")           

def date():
    Date=dt.datetime.now().day
    Month=dt.datetime.now().month
    Year=dt.datetime.now().year
    speak(Date)
    speak(Month)
    speak(Year)

def wishme():
    hour=dt.datetime.now().hour
    if(hour>=6 and hour<12):
        speak("good morning sir")
    elif(hour>=12 and hour<18):
        speak("good afternoon sir")
    elif(hour>=18 and hour<24):
        speak("good evening sir")
    else:
        speak("good night sir")            

    speak("what can i do for you !!")

def opencam():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow("naman",frame)
        cv2.waitKey(1)
    cv2.destroyAllWindows()  
    cap.release()
def shut():
    speak("computer going to sleep")
    os.system('shutdown /s /t 1') 
def restart():
    speak("restarting computer")
    os.system('shutdown /r /t 1')        

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        speak("recognizing sir...")
        query=r.recognize_google(audio,language="en-in")
        
    except Exception as e:
        return "None"
      

    return query
       
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        print(query)
        if "time" in query:
            time()
        if "date" in query:
            date()
        if "camera" in query:
            opencam() 
        if "offline" in query:
            speak("good bye sir")
            quit() 
        if "notepad" in query:
            note() 
        if "shutdown" in query:
            shut()
        if "restart" in query:
            restart()
        if "wordpad" in query:
            wordpad()                         
                    

