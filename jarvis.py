
import pyttsx3
import speech_recognition as sr
import datetime as dt
import cv2
import subprocess
import webbrowser as wb
import os
import wikipedia
import pyautogui

engine=pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def startcode():
    os.system(command="code")
    
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
        speak('hello sir')
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

def log():
    speak("loging out sir")
    os.system("shutdown -l")

def start():
    pyautogui.keyDown('winleft')
    pyautogui.keyUp('winleft')

def caps():
    pyautogui.keyDown('capslock')
    pyautogui.keyUp('capslock')

def jokes():
    speak(pyjokes.get_joke())    


def shut():
    speak("computer going to sleep")
    os.system('shutdown /s /t 1') 

def restart():
    speak("restarting computer")
    os.system('shutdown /r /t 1')


def cpu():
    usage=str(psutil.cpu_percent())
    speak('cpu is at'+usage)  
    battery=psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent) 

def google():
    speak("what should i search sir in google")
    chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    search=takecommand().lower()
    print(search)
    search=search.replace('/',' ')
    if search!="none":
        speak("opening "+search)
        wb.get(chromepath).open_new_tab(search)
    else:
        google() 

def remember1():
    speak("what should i remember")
    data=takecommand().lower()
    if data!="none":
        remember=open('data.txt','w')
        remember.write(data)
        remember.close()
        speak("remembered sir")
    else:
        remember1()                             

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        speak('listening')
        audio=r.listen(source)
    try:
        print('recognizing')
        query=r.recognize_google(audio,language="en-us")
        
    except Exception as e:
        return "None"
      

    return query
       
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        print(query)
        '''
            myDict = {
                "time":time,
                "date":date,
                "camera":opencam,
                "notepad":note,
                "shutdown":shut,
                "restart":restart,
                "wordpad":wordpad,
                "screenshot":screen,
                "logout":log,
                "windows":start,
                "lock":caps
                "code":startcode,
                "jokes":jokes,
                "cpu":cpu,
                "google":google,
                "remember":remember1
            }
            for i in myDict.keys():
                if i in query:
                    myDict[i]()
                
        '''
        
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "camera" in query:
            opencam() 
        ####
        elif "sleep" in query:
            speak("good bye sir")
            quit() 
        ####
        elif "notepad" in query:
            note() 
        elif "shutdown" in query:
            shut()
        elif "restart" in query:
            restart()
        elif "wordpad" in query:
            wordpad()
        #####
        elif "wikipedia" in query:
            wiki(query)
        #####
        elif "screenshot" in query:
            screen()
        elif "logout" in query:
            log()
        elif "windows" in query:
            start() 
        elif "lock" in query:
            caps() 
        elif "thank" in query:
            speak("its ok sir")
        elif "code" in query:
            startcode()
        elif "firefox" in query:
            os.system(command="start firefox.exe") 
        elif "jokes" in query:
            jokes() 
        elif "cpu" in query:
            cpu()
        elif "google" in query:
            google()

        elif "remember" in query:
            remember1()
###
        elif "know" in query:
            remember=open('data.txt','r')
            speak(remember.read())        
###
            
                    
