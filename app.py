import pyttsx3 as p
import speech_recognition as sr
from selenium_webdriver import infow
from selenium import webdriver

engine = p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',190)
voices=engine.getProperty('voices')
engine.setProperty('voice'.voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r= sr.Recognizer()

speak("hello iam your voice assicient")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    audio= r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
#     speak("i am having a good day sir")
# speak("what can i do for you")  
    with sr.Microphone() as source:
        r.energy_threshold=10000
    
    r.adjust_for_ambient_noise(source,1.2)
    print("listening....") 
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    
if "information" in text2:
    speak("you need information relatedn to which topic")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening....") 
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor) 

