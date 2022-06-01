import tkinter as Tk
from tkinter import *
from turtle import Screen, bgcolor
from tkinter import ttk
import tkinter.messagebox
import os
import pandas as pd

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("925x500+300+200")
    screen.title("Presensi Mahasiswa")
    screen.configure(bg="#fff")

    sekolah_bg=PhotoImage(file="sekolah.png")
    sekolah=Label(screen,image=sekolah_bg,bg="white")
    sekolah.place(x=0,y=0)  

    Label(screen,text="Selamat Datang di Universitas Internasional", font=("Acumin Variable Concept",20,"bold"),bg="white").place(x=372,y=20)
    
    #Frame(screen,width=400, height=2,bg="#f3f5f6").place(x=25,y=80)

    dosen_image=PhotoImage(file="dosen.png")
    icondosen=Button(screen,image=dosen_image,command=dosen_login)
    icondosen.place(x=440,y=200)

    mahasiswa_image=PhotoImage(file="student.png")
    iconmahasiswa=Button(screen,image=mahasiswa_image,command=mahasiswa_login)
    iconmahasiswa.place(x=785,y=200)

    Label(screen,text="Dosen",font=("Acumin Variable Concept",17,"bold"),bg="white").place(x=452,y=310)
    Label(screen,text="Mahasiswa",font=("Acumin Variable Concept",17,"bold"),bg="white").place(x=770,y=310)
   
    screen.mainloop()

def mahasiswa_login():
    global screen2, namamahasiswa, nimmahasiswa, labelmahasiswa
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("925x500+300+200")
    screen2.configure(bg="#fff")
    #screen2.resizable(False,False)

    #img = PhotoImage(file="login.png")
    #login=Label(screen2,image=img,bg="white")
    #login.place(x=50,y=50)

    frame=Frame(screen2,width=350,height=350,bg="white")
    frame.place(x=480,y=70)
    
    heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=119,y=5)

########--------------------------------------------------------------------------
    def on_enter(e):
        namamahasiswa.delete(0, "end")

    def on_leave(e):
        name=namamahasiswa.get()
        if name=="":
            namamahasiswa.insert(0,"Nama Lengkap")

    namamahasiswa = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    namamahasiswa.place(x=30,y=80)
    namamahasiswa.insert(0,"Nama Lengkap")
    namamahasiswa.bind("<FocusIn>", on_enter)
    namamahasiswa.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

########--------------------------------------------------------------------------
    def on_enter(e):
        nimmahasiswa.delete(0, "end")

    def on_leave(e):
        name=nimmahasiswa.get()
        if name=="":
            nimmahasiswa.insert(0,"Nomor Induk Mahasiswa")

    nimmahasiswa = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    nimmahasiswa.place(x=30,y=150)
    nimmahasiswa.insert(0,"Nomor Induk Mahasiswa")
    nimmahasiswa.bind("<FocusIn>", on_enter)
    nimmahasiswa.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########___________________________________________________________________________############

    Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0, command=loginmahasiswa_verify).place(x=35,y=204)

    labelmahasiswa=Label(screen2)
    labelmahasiswa.pack()

def dosen_login():
    global screen3, namadosen, niddosen, labeldosen
    screen3=Toplevel(screen)
    screen3.title("Login")
    screen3.geometry("925x500+300+200")
    screen3.configure(bg="#fff")
    #screen3.resizable(False,False)
    
    #img = PhotoImage(file="login.png")
    #Label(screen3,image=img,bg="white").place(x=50,y=50)

    frame=Frame(screen3,width=350,height=350,bg="white")
    frame.place(x=480,y=70)
    
    heading=Label(frame,text="Sign In",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=119,y=5)

########--------------------------------------------------------------------------
    def on_enter(e):
        namadosen.delete(0, "end")

    def on_leave(e):
        name=namadosen.get()
        if name=="":
            namadosen.insert(0,"Nama Lengkap")

    namadosen = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    namadosen.place(x=30,y=80)
    namadosen.insert(0,"Nama Lengkap")
    namadosen.bind("<FocusIn>", on_enter)
    namadosen.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)

########--------------------------------------------------------------------------
    def on_enter(e):
        niddosen.delete(0, "end")

    def on_leave(e):
        name=niddosen.get()
        if name=="":
            niddosen.insert(0,"Nomor Induk Dosen")

    niddosen = Entry(frame,width=36,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    niddosen.place(x=30,y=150)
    niddosen.insert(0,"Nomor Induk Dosen")
    niddosen.bind("<FocusIn>", on_enter)
    niddosen.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########___________________________________________________________________________############

    Button(frame,width=39,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0, command=logindosen_verify).place(x=35,y=204)

    labeldosen=Label(screen3)
    labeldosen.pack()

def loginmahasiswa_verify():
    userData = pd.read_csv('datamahasiswa.csv')
    df = pd.DataFrame(userData)

    inputnama = namamahasiswa.get().upper()
    inputnim = nimmahasiswa.get().upper()

    mc = (len(df[(df.Nama_Lengkap == inputnama) & (df.NIM == inputnim)]) > 0)
    if mc:
        labelmahasiswa.configure(text="Berhasil")
        menumahasiswa()
    else:
        labelmahasiswa.configure(text="Gagal")

def logindosen_verify():
    userData = pd.read_csv('datadosen.csv')
    df = pd.DataFrame(userData)

    inputdosen = namadosen.get().upper()
    inputnid = niddosen.get().upper()

    mc = (len(df[(df.Nama_dosen == inputdosen) & (df.NID == inputnid)]) > 0)
    if mc:
        labeldosen.configure(text="Berhasil")
        menudosen()
    else:
        labeldosen.configure(text="Gagal")

def menudosen():
    global screen4
    screen4=Toplevel(screen)
    screen4.geometry("300x250")
    screen4.title("Menu Dosen")
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Membuat Presensi", bg="grey", width="30", height="2", command=membuat_presensi).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Melihat Presensi", bg="grey", width="30", height="2", command=melihat_presensi).pack()
    Label(screen4, text="").pack()
    
def membuat_presensi():
    global screen5
    screen5=Toplevel(screen)
    screen5.geometry("500x550")
    screen5.title("Membuat Presensi")
    Button(screen5, text="Programa Komputer", width="30", height="2", command=prokom).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Kalkulus", width="30", height="2", command=kalkulus).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Fisika Dasar", width="30", height="2", command=fisdas).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Anggaran dan Estimasi Biaya", width="30", height="2", command=AEB).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Material Teknik", width="30", height="2", command=mattek).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Mekanika Teknik", width="30", height="2", command=mekatek).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Perancangan dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen5, text="").pack()

def prokom():
    print()
    
def kalkulus():
    print()

def AEB():
    print()

def PRD():
    print()

def psikin():
    print()

def mekatek():
    print()

def mattek():
    print()

def fisdas():
    print()

def bio():
    print()

def melihat_presensi():
    print()

def menumahasiswa():
    global screen6
    screen6=Toplevel(screen)
    screen6.geometry("500x550")
    screen6.title("Membuat Presensi")
    Button(screen6, text="Programa Komputer", width="30", height="2", command=prokom).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Kalkulus", width="30", height="2", command=kalkulus).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Fisika Dasar", width="30", height="2", command=fisdas).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Anggaran dan Estimasi Biaya", width="30", height="2", command=AEB).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Material Teknik", width="30", height="2", command=mattek).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Mekanika Teknik", width="30", height="2", command=mekatek).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Perancangan dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen6, text="").pack()

main_screen()