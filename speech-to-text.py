from tkinter import *
import speech_recognition as sr
import pyaudio
import pyttsx3
import threading

def speechToText():
    while True:
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                #sr.adjust_for_ambient_noise(source,duration=0.2)
                audio = recognizer.listen(source)
                query=recognizer.recognize_google(audio)
                print('You said : {}'.format(query))
                query=query.capitalize()

                questionField.delete(0,END)
                questionField.insert(0,query)

        except Exception as e:
            print(e)

root = Tk()
root.title("Speech-to-Text")
root.geometry("500x230")
root['background']='navajo white'

Label(root, text="Speech to Text!", bg="navajo white", font=("Helventica 30 bold"), fg="saddle brown").pack(pady=30)

Label(root, text="Recognized Speech:", bg="navajo white", font=("Helventica 12")).pack(pady=5)

questionField=Entry(root,font=('verdana',20,'bold'))
questionField.pack(pady=12)

Label(root, text="Tayal", bg="navajo white", font=("Helventica 8")).pack(pady=5)

thread= threading.Thread(target=speechToText)
thread.setDaemon(True)
thread.start()


root.mainloop()