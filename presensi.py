from cProfile import label
import tkinter as Tk
from tkinter import *
from turtle import Screen, bgcolor, clear
from tkinter import ttk
import tkinter.messagebox
import os
from numpy import imag
import pandas as pd
from PIL import ImageTk, Image

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("925x500+300+200")
    screen.title("SSO Universitas Internasional")
    screen.configure(bg="#fff")

    sekolah_bg=PhotoImage(file="sekolahui.png")
    sekolah=Label(screen,image=sekolah_bg,bg="white")
    sekolah.place(x=0,y=0)  

    Label(screen,text="Selamat Datang di Universitas Internasional", font=("Acumin Variable Concept",20,"bold"),bg="white").place(x=372,y=20)
    
    #Frame(screen,width=400, height=2,bg="#f3f5f6").place(x=25,y=80)

    dosen_image=PhotoImage(file="dosen.png")
    icondosen=Button(screen,image=dosen_image,bg="#fff",command=dosen_login)
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
    screen2.title("Login SSO Mahasiswa")
    screen2.geometry("925x500+300+200")
    screen2.configure(bg="white")
    #screen2.resizable(False,False)

    #framelogin=Frame(screen2, width=400, height=600)
    #framelogin.pack()
    #framelogin.place(anchor="center",relx=0.5,rely=0.5)
    #img=ImageTk.PhotoImage(Image.open("login.png"))
    #label=Label(framelogin,image=img)
    #label.pack()
    
    img = PhotoImage(file="login.png")
    bgmahasiswa=Label(screen2,image=img,bg="white")
    bgmahasiswa.place(x=50,y=50)

    frame=Frame(screen2,width=360,height=350,bg="white")
    frame.place(x=480,y=70)
    
    heading=Label(frame,text="Single Sign On (SSO)",fg="black",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=20,y=25)

    Label(frame,text="Masukkan Nama Lengkap dan Nomor Induk Mahasiswa Anda", font=("times new roman",9),bg="white").place(x=30,y=100)
    Label(frame,text="Enter your full name and Student ID Number", font=("times new roman",9,"italic"),bg="white").place(x=30,y=120)
    
   
########--------------------------------------------------------------------------
    def on_enter(e):
        namamahasiswa.delete(0, "end")

    def on_leave(e):
        name=namamahasiswa.get()
        if name=="":
            namamahasiswa.insert(0,"Nama Lengkap")

    namamahasiswa = Entry(frame,width=37,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    namamahasiswa.place(x=30,y=150)
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

    nimmahasiswa = Entry(frame,width=37,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    nimmahasiswa.place(x=30,y=200)
    nimmahasiswa.insert(0,"Nomor Induk Mahasiswa")
    nimmahasiswa.bind("<FocusIn>", on_enter)
    nimmahasiswa.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########___________________________________________________________________________############

    Button(frame,width=40,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0, command=loginmahasiswa_verify).place(x=35,y=254)

    labelmahasiswa=Label(frame, bg="white")
    labelmahasiswa.place(x=152,y=294)
    screen2.mainloop()

def dosen_login():
    global screen3, namadosen, niddosen, labeldosen
    screen3=Toplevel(screen)
    screen3.title("Login SSO Dosen")
    screen3.geometry("925x500+300+200")
    screen3.configure(bg="white")
    #screen3.resizable(False,False)

    imgg = PhotoImage(file="vector.png")
    bgdosen=Label(screen3,image=imgg,bg="white")
    bgdosen.place(x=50,y=50)

    frame1=Frame(screen3,width=360,height=350,bg="white")
    frame1.place(x=480,y=70)
    
    heading=Label(frame1,text="Single Sign On (SSO)",fg="black",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
    heading.place(x=20,y=25)

    Label(frame1,text="Masukkan Nama Lengkap dan Nomor Induk Dosen Anda", font=("times new roman",9),bg="white").place(x=30,y=100)
    Label(frame1,text="Enter your full name and Lecturer ID Number", font=("times new roman",9,"italic"),bg="white").place(x=30,y=120)

########--------------------------------------------------------------------------
    def on_enter(e):
        namadosen.delete(0, "end")

    def on_leave(e):
        name=namadosen.get()
        if name=="":
            namadosen.insert(0,"Nama Lengkap")

    namadosen = Entry(frame1,width=37,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    namadosen.place(x=30,y=150)
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

    niddosen = Entry(frame1,width=37,fg="black",border=2,bg="white",font=("Microsoft YaHei UI Light",11))
    niddosen.place(x=30,y=200)
    niddosen.insert(0,"Nomor Induk Dosen")
    niddosen.bind("<FocusIn>", on_enter)
    niddosen.bind("<FocusOut>", on_leave)

    #Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)

########___________________________________________________________________________############

    Button(frame1,width=40,pady=7,text="Sign In",bg="#57a1f8",fg="white",border=0, command=logindosen_verify).place(x=35,y=254)

    labeldosen=Label(frame1, bg="white")
    labeldosen.place(x=152,y=294)
    screen3.mainloop()

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
    screen4.geometry("925x500+300+200")
    screen4.title("SSO Universitas Internasional")
    screen4.configure(bg="#fff")

    frame2=Frame(screen4,width=400,height=400,bg="grey")
    frame2.place(x=400,y=70)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(frame2,image=bgdosen,bg="white")
    backgroundosen.place(x=0,y=0)

    Button(screen4,text="Membuat Presensi",font=("Acumin Variable Concept",17,"bold"),bg="white", command=membuat_presensi).place(x=400,y=500)
    Button(screen4,text="Melihat Presensi",font=("Acumin Variable Concept",17,"bold"),bg="white", command=melihat_presensi).place(x=685,y=500)
    #Button(screen4, text="Membuat Presensi", bg="grey", width="30", height="2", command=membuat_presensi)
    #Button(screen4, text="Melihat Presensi", bg="grey", width="30", height="2", command=melihat_presensi)
    screen4.mainloop()

def membuat_presensi():
    global screen5
    screen5=Toplevel(screen)
    screen5.geometry("500x550")
    screen5.title("Membuat Presensi")
    Button(screen5, text="Programa Komputer", width="30", height="2", command=membuatprokom).pack()
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
    Button(screen5, text="Pengantar Rekayasa dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen5, text="").pack()

def membuatprokom():
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
    Button(screen6, text="Programa Komputer", width="30", height="2", command=membuatprokom).pack()
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
    Button(screen6, text="PPengantar Rekayasa dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen6, text="").pack()

main_screen()