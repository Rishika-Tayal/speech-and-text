from tkinter import *
import pyttsx3

root = Tk()
root.title("Text-to-Speech")
root.geometry("500x285")
root['background']='sky blue'

def speech():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text.get())
    engine.runAndWait()
    text.delete(0,END)

Label(root, text="Text to Speech!", bg="sky blue", font=("Helventica 30 bold"), fg="blue4").pack(pady=20)

Label(root, text="Type something:", bg="sky blue", font=("Helventica 12")).pack(pady=5)
text = Entry(root, font=("Helventica", 28))
text.pack(pady=10)

my_button = Button(root, font=("Helventica 15 bold"), bg='black', fg='#fff', text= "Convert to Speech", command=speech)
my_button.pack(pady=10)

Label(root, text="Tayal", bg="sky blue", font=("Helventica 8")).pack(pady=8)


root.mainloop()