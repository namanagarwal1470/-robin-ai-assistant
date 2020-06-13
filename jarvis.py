import pyttsx3
import speech_recognition as sr
import datetime as dt
import cv2
import subprocess
import os
import wikipedia
import pyautogui

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

def screen():
    img=pyautogui.screenshot()
    img.save("C:\\Users\\Naman\\Desktop\\image.png")
    os.system(command="C:\\Users\\Naman\\Desktop\\image.png")


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

def wiki(query1):
    speak("searching in wikipedia..")
    query1=query1.replace("wikipedia","")
    result=wikipedia.summary(query1,sentences=2)   
    speak(result)
    print(query)


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
        elif "date" in query:
            date()
        elif "camera" in query:
            opencam() 
        elif "offline" in query:
            speak("good bye sir")
            quit() 
        elif "notepad" in query:
            note() 
        elif "shutdown" in query:
            shut()
        elif "restart" in query:
            restart()
        elif "wordpad" in query:
            wordpad()
        elif "wikipedia" in query:
            wiki(query)
        elif "screenshot" in query:
            screen()
                    

