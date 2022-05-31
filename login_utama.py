from cProfile import label
import code
import fractions
import py_compile
from tkinter import *
from tkinter import messagebox
from webbrowser import get
from xml.dom.expatbuilder import FragmentBuilder
import pandas as pd

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

def loginmahasiswa_verify():
    userData = pd.read_csv('datamahasiswa.csv')
    df = pd.DataFrame(userData)

    inputnama = user.get().upper()
    inputnim = code.get().upper()

    mc = (len(df[(df.Nama_Lengkap == inputnama) & (df.NIM == inputnim)]) > 0)
    if mc:
        labelhasil.configure(text="Berhasil")
        menumahasiswa()
    else:
        labelhasil.configure(text="Gagal")

img = PhotoImage(file="login.png")
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=100,y=5)

########--------------------------------------------------------------------------
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Nama Lengkap")

user = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Nama Lengkap")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

########--------------------------------------------------------------------------
def on_enter(e):
    code.delete(0, "end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"NIM")

code = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"NIM")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########___________________________________________________________________________############

Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0).place(x=35,y=204)

root.mainloop()