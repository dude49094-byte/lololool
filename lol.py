from tkinter import *
import random
a=random.randint(1,100)
root=Tk()
root["bg"]="gray"
root.title("game")
def ok():
    global lab
    user=ent.get()
    try:
        if int(user)>a:
            lab.configure(text="smaller")
        elif int(user)<a:
            lab.configure(text="bigger")
        elif int(user)==a:
            lab.configure(text="you won!")
    except ValueError:
        lab.configure(text="idiot,enter numbers")
    ent.delete(0,END)
btn=Button(root,text="press",command=ok)
btn.pack()
ent=Entry(root)
ent.pack()
lab=Label(root,text="bigger or smal")
lab.pack()
root.mainloop()