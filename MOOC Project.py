import tkinter
from tkinter import * 
from textblob import TextBlob

root = Tk ()
root.title("Morag's Spell Checker")
root.geometry ("650x400") 
root.config (background= "#826F66")

def check_spelling ():
    word=enter_text.get()
    a = TextBlob(word)
    right=str(a.correct())
    cs=Label (root, text= "The correct spelling is:", font = ("Arial", 14, "bold"),bg= "#826F66", fg = "#3A3845" )
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label (root, text = "Can you even spell, bro?", font = ("Arial", 20, "bold" ), bg = "#826F66", fg = "#3A3845")
heading.pack (pady= (50,0))
enter_text= Entry (root, justify="center", width= 30, font= ("Arial", 20, "bold"), bg= "white", border=2)
enter_text.pack (pady= 10)
enter_text.focus()

Button=Button(root, text= "Check", font= ("Arial", 16, "bold"), fg= "#A0C1B8", bg="#351F39", command= check_spelling)
Button.pack()

spell=Label(root, font= ("Arial",14), bg="#826F66", fg="#A0C1B8")
spell.place(x=350, y=250)

root.mainloop ()

#my first attempt at proper coding- still don't know what it all does, but it works!!!!