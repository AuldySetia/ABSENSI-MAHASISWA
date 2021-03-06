from cProfile import label
import csv
import tkinter as Tk
from tkinter import *
from turtle import Screen, bgcolor, clear
from tkinter import ttk
import tkinter.messagebox
import os
from numpy import imag
import csv
import pandas as pd
from tkinter import ttk

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("1280x720")
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
    screen2.geometry("1280x720")
    screen2.configure(bg="white")

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
    screen3.geometry("1280x720")
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
    screen4.geometry("1280x720")
    screen4.title("SSO Universitas Internasional")
    screen4.configure(bg="#fff")

    frame2=Frame(screen4,width=400,height=400,bg="grey")
    frame2.place(x=400,y=70)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(frame2,image=bgdosen,bg="white")
    backgroundosen.place(x=0,y=0)

    Button(screen4,text="Membuat Presensi",font=("Acumin Variable Concept",17,"bold"),bg="white", command=membuat_presensi).place(x=400,y=500)
    Button(screen4,text="Melihat Presensi",font=("Acumin Variable Concept",17,"bold"),bg="white", command=melihat_presensi).place(x=685,y=500)

    screen4.mainloop()

def membuat_presensi():
    global screen5
    screen5=Toplevel(screen)
    screen5.geometry("1280x720")
    screen5.title("Membuat Presensi")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen5,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen5,text="MATA KULIAH",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)
    
    Button(screen5,text="PROGRAMA KOMPUTER", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mprokom).place(x=20,y=170)
    Button(screen5,text="KALKULUS", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mkalkulus).place(x=430,y=170)
    Button(screen5,text="FISIKA DASAR II", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mfisdas).place(x=835,y=170)
    Button(screen5,text="ANALISIS & ESTIMASI BIAYA", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mAEB).place(x=20,y=320)
    Button(screen5,text="MATERIAL TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mmattek).place(x=430,y=320)
    Button(screen5,text="MEKANIKA TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mmekatek).place(x=835,y=320)
    Button(screen5,text="PENGANTAR REKAYASA & DESAIN", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mPRD).place(x=20,y=470)
    Button(screen5,text="PSIKOLOGI INDUSTRI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mpsikin).place(x=430,y=470)
    Button(screen5,text="BIOLOGI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mbio).place(x=835,y=470)

    screen5.mainloop()


def mprokom():
    global screen8, defprokom
    screen8=Toplevel(screen)
    screen8.geometry("1280x720")
    screen8.title("Keterangan Pertemuan")
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="").pack()
    Label(screen8, text="Input Pertemuan").pack()
    defprokom=Entry(screen8)
    defprokom.pack()
    Label(screen8, text="").pack()
    Button(screen8, text="SUBMIT", width=10, height=1, command=saveprokom).pack()

def saveprokom():
    global namafile, csvheader, writer
    save_path = "Prokom"
    namafile = os.path.join(save_path, f'Pertemuan {defprokom.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None

        
def mkalkulus():
    global screen10, defkalkulus
    screen10=Toplevel(screen)
    screen10.geometry("1280x720")
    screen10.title("Kalkulus")
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Input Pertemuan").pack()
    defkalkulus=Entry(screen10)
    defkalkulus.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="SUBMIT", width=10, height=1, command=savekalkulus).pack()

def savekalkulus():
    global namafile, csvheader, writer
    save_path = "Kalkulus"
    namafile = os.path.join(save_path, f'Pertemuan {defkalkulus.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mAEB():
    global screen11, defAEB
    screen11=Toplevel(screen)
    screen11.geometry("1280x720")
    screen11.title("Analisis dan Estimasi Biaya")
    Label(screen11, text="").pack()
    Label(screen11, text="").pack()
    Label(screen11, text="").pack()
    Label(screen11, text="Input Pertemuan").pack()
    defAEB=Entry(screen11)
    defAEB.pack()
    Label(screen11, text="").pack()
    Button(screen11, text="SUBMIT", width=11, height=1, command=saveAEB).pack()

def saveAEB():
    global namafile, csvheader, writer
    save_path = "AEB"
    namafile = os.path.join(save_path, f'Pertemuan {defAEB.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mPRD():
    global screen12, defPRD
    screen12=Toplevel(screen)
    screen12.geometry("1280x720")
    screen12.title("Pengantar Rekayasa dan Desain")
    Label(screen12, text="").pack()
    Label(screen12, text="").pack()
    Label(screen12, text="").pack()
    Label(screen12, text="Input Pertemuan").pack()
    defPRD=Entry(screen12)
    defPRD.pack()
    Label(screen12, text="").pack()
    Button(screen12, text="SUBMIT", width=12, height=1, command=savePRD).pack()

def savePRD():
    global namafile, csvheader, writer
    save_path = "PRD"
    namafile = os.path.join(save_path, f'Pertemuan {defPRD.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mpsikin():
    global screen13, defpsikin
    screen13=Toplevel(screen)
    screen13.geometry("1280x720")
    screen13.title("Psikologi Industri")
    Label(screen13, text="").pack()
    Label(screen13, text="").pack()
    Label(screen13, text="").pack()
    Label(screen13, text="Input Pertemuan").pack()
    defpsikin=Entry(screen13)
    defpsikin.pack()
    Label(screen13, text="").pack()
    Button(screen13, text="SUBMIT", width=13, height=1, command=savepsikin).pack()

def savepsikin():
    global namafile, csvheader, writer
    save_path = "Psikin"
    namafile = os.path.join(save_path, f'Pertemuan {defpsikin.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mmekatek():
    global screen14, defmekatek
    screen14=Toplevel(screen)
    screen14.geometry("1280x720")
    screen14.title("Mekanika Teknik")
    Label(screen14, text="").pack()
    Label(screen14, text="").pack()
    Label(screen14, text="").pack()
    Label(screen14, text="Input Pertemuan").pack()
    defmekatek=Entry(screen14)
    defmekatek.pack()
    Label(screen14, text="").pack()
    Button(screen14, text="SUBMIT", width=14, height=1, command=savemekatek).pack()

def savemekatek():
    global namafile, csvheader, writer
    save_path = "Mekatek"
    namafile = os.path.join(save_path, f'Pertemuan {defmekatek.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mmattek():
    global screen15, defmattek
    screen15=Toplevel(screen)
    screen15.geometry("1280x720")
    screen15.title("Material Teknik")
    Label(screen15, text="").pack()
    Label(screen15, text="").pack()
    Label(screen15, text="").pack()
    Label(screen15, text="Input Pertemuan").pack()
    defmattek=Entry(screen15)
    defmattek.pack()
    Label(screen15, text="").pack()
    Button(screen15, text="SUBMIT", width=15, height=1, command=savemattek).pack()

def savemattek():
    global namafile, csvheader, writer
    save_path = "Mattek"
    namafile = os.path.join(save_path, f'Pertemuan {defmattek.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None


def mfisdas():
    global screen16, deffisdas
    screen16=Toplevel(screen)
    screen16.geometry("1280x720")
    screen16.title("Fisika Dasar II")
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Input Pertemuan").pack()
    deffisdas=Entry(screen16)
    deffisdas.pack()
    Label(screen16, text="").pack()
    Button(screen16, text="SUBMIT", width=16, height=1, command=savefisdas).pack()

def savefisdas():
    global namafile, csvheader, writer
    save_path = "Fisdas"
    namafile = os.path.join(save_path, f'Pertemuan {deffisdas.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            

def mbio():
    global screen16, defbio
    screen16=Toplevel(screen)
    screen16.geometry("1280x720")
    screen16.title("Biologi")
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Input Pertemuan").pack()
    defbio=Entry(screen16)
    defbio.pack()
    Label(screen16, text="").pack()
    Button(screen16, text="SUBMIT", width=16, height=1, command=savebio).pack()

def savebio():
    global namafile, csvheader, writer
    save_path = "Bio"
    namafile = os.path.join(save_path, f'Pertemuan {defbio.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
        
def melihat_presensi():
    global screen10
    screen10=Toplevel(screen)
    screen10.geometry("1280x720")
    screen10.title("Melihat Presensi")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen10,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen10,text="MATA KULIAH",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)
    
    Button(screen10,text="PROGRAMA KOMPUTER", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lprokom).place(x=20,y=170)
    Button(screen10,text="KALKULUS", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lkalkulus).place(x=430,y=170)
    Button(screen10,text="FISIKA DASAR II", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lfisdas).place(x=835,y=170)
    Button(screen10,text="ANALISIS & ESTIMASI BIAYA", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lAEB).place(x=20,y=320)
    Button(screen10,text="MATERIAL TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lmattek).place(x=430,y=320)
    Button(screen10,text="MEKANIKA TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lmekatek).place(x=835,y=320)
    Button(screen10,text="PENGANTAR REKAYASA & DESAIN", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lPRD).place(x=20,y=470)
    Button(screen10,text="PSIKOLOGI INDUSTRI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lpsikin).place(x=430,y=470)
    Button(screen10,text="BIOLOGI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=lbio).place(x=835,y=470)

    screen10.mainloop()

def lprokom():
    global screen26, mmb7
    screen26=Toplevel(screen)
    screen26.geometry("1280x720")
    screen26.title("SSO UNIVERSITAS INTERNASIONAL")
    screen26.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen26,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen26,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb7=ttk.Combobox(frame,value=course,width=15)
    mmb7.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showprokom).place(x=35,y=254) 
    mmb7.current(0)

    screen26.mainloop()
def showprokom():
    screen35 = Toplevel(screen)
    screen35.title("SSO UNIVERSITAS INTERNASIONAL")
    screen35.geometry("1280x720")
    screen35.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen35,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)


    title=Label(screen35,text="Hasil Presensi Mata Kuliah Programa Komputer",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen35, width=100)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=100, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack(expand=None)
    tree.pack_propagate(0)

    save_path = "Prokom"
    namafile = os.path.join(save_path, f'{mmb7.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen35.mainloop()

def lkalkulus():
    global screen27,mmb3
    screen27=Toplevel(screen)
    screen27.geometry("1280x720")
    screen27.title("SSO UNIVERSITAS INTERNASIONAL")
    screen27.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen27,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen27,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb3=ttk.Combobox(frame,value=course,width=15)
    mmb3.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showkalkulus).place(x=35,y=254) 
    mmb3.current(0)

    screen27.mainloop()

def showkalkulus():
    screen36 = Toplevel(screen)
    screen36.title("SSO UNIVERSITAS INTERNASIONAL")
    screen36.geometry("1280x720")
    screen36.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen36,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)


    title=Label(screen36,text="Hasil Presensi Mata Kuliah Kalkulus",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen36, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Kalkulus"
    namafile = os.path.join(save_path, f'{mmb3.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen36.mainloop()

def lfisdas():
    global screen28, mmb2
    screen28=Toplevel(screen)
    screen28.geometry("1280x720")
    screen28.title("SSO UNIVERSITAS INTERNASIONAL")
    screen28.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen28,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen28,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb2=ttk.Combobox(frame,value=course,width=15)
    mmb2.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showfisdas).place(x=35,y=254) 
    mmb2.current(0)

    screen28.mainloop()

def showfisdas():
    screen37 = Toplevel(screen)
    screen37.title("SSO UNIVERSITAS INTERNASIONAL")
    screen37.geometry("1280x720")
    screen37.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen37,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen37,text="Hasil Presensi Mata Kuliah Fisika Dasar",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen37, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Fisdas"
    namafile = os.path.join(save_path, f'{mmb2.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen37.mainloop()

def lAEB():
    global screen29, mmb
    screen29=Toplevel(screen)
    screen29.geometry("1280x720")
    screen29.title("SSO UNIVERSITAS INTERNASIONAL")
    screen29.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen29,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen29,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb=ttk.Combobox(frame,value=course,width=15)
    mmb.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showAEB).place(x=35,y=254) 
    mmb.current(0)

    screen26.mainloop()
def showAEB():
    screen38 = Toplevel(screen)
    screen38.title("SSO UNIVERSITAS INTERNASIONAL")
    screen38.geometry("1280x720")
    screen38.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen38,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)


    title=Label(screen38,text="Hasil Presensi Mata Kuliah Analisis Estimasi dan Biaya",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen38, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "AEB"
    namafile = os.path.join(save_path, f'{mmb.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen38.mainloop()

def lmattek():
    global screen30, mmb4
    screen30=Toplevel(screen)
    screen30.geometry("1280x720")
    screen30.title("SSO UNIVERSITAS INTERNASIONAL")
    screen30.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen30,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen30,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb4=ttk.Combobox(frame,value=course,width=15)
    mmb4.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showmattek).place(x=35,y=254) 
    mmb4.current(0)

    screen30.mainloop()
def showmattek():
    screen39 = Toplevel(screen)
    screen39.title("SSO UNIVERSITAS INTERNASIONAL")
    screen39.geometry("1280x720")
    screen39.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen39,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen39,text="Hasil Presensi Mata Kuliah Material Teknik",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen39, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Mattek"
    namafile = os.path.join(save_path, f'{mmb4.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen39.mainloop()

def lmekatek():
    global screen31, mmb5
    screen31=Toplevel(screen)
    screen31.geometry("1280x720")
    screen31.title("SSO UNIVERSITAS INTERNASIONAL")
    screen31.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen31,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen31,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb5=ttk.Combobox(frame,value=course,width=15)
    mmb5.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showmekatek).place(x=35,y=254) 
    mmb5.current(0)

    screen31.mainloop()

def showmekatek():
    screen40 = Toplevel(screen)
    screen40.title("SSO UNIVERSITAS INTERNASIONAL")
    screen40.geometry("1280x720")
    screen40.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen40,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)


    title=Label(screen40,text="Hasil Presensi Mata Kuliah Mekanika Teknik",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen40, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Mekatek"
    namafile = os.path.join(save_path, f'{mmb5.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen40.mainloop()

def lPRD():
    global screen32, mmb6
    screen32=Toplevel(screen)
    screen32.geometry("1280x720")
    screen32.title("SSO UNIVERSITAS INTERNASIONAL")
    screen32.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen32,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen32,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb6=ttk.Combobox(frame,value=course,width=15)
    mmb6.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showPRD).place(x=35,y=254) 
    mmb6.current(0)

    screen32.mainloop()
def showPRD():
    screen41 = Toplevel(screen)
    screen41.title("SSO UNIVERSITAS INTERNASIONAL")
    screen41.geometry("1280x720")
    screen41.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen41,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen41,text="Hasil Presensi Mata Kuliah Pengantar Rekayasa Desain",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)    

    TableMargin = Frame(screen41, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "PRD"
    namafile = os.path.join(save_path, f'{mmb6.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen41.mainloop()

def lpsikin():
    global screen33, mmb8
    screen33=Toplevel(screen)
    screen33.geometry("1280x720")
    screen33.title("SSO UNIVERSITAS INTERNASIONAL")
    screen33.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen33,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen33,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb8=ttk.Combobox(frame,value=course,width=15)
    mmb8.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showpsikin).place(x=35,y=254) 
    mmb8.current(0)

    screen33.mainloop()
def showpsikin():
    screen42 = Toplevel(screen)
    screen42.title("SSO UNIVERSITAS INTERNASIONAL")
    screen42.geometry("1280x720")
    screen42.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen42,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen42,text="Hasil Presensi Mata Kuliah Psikologi Industri",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen42, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Psikin"
    namafile = os.path.join(save_path, f'{mmb8.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen42.mainloop()

def lbio():
    global screen34, mmb1
    screen34=Toplevel(screen)
    screen34.geometry("1280x720")
    screen34.title("SSO UNIVERSITAS INTERNASIONAL")
    screen34.configure(bg="white")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen34,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)
    frame=Frame(screen34,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    mmb1=ttk.Combobox(frame,value=course,width=15)
    mmb1.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=showbio).place(x=35,y=254) 
    mmb1.current(0)

    screen34.mainloop()

def showbio():
    screen43 = Toplevel(screen)
    screen43.title("SSO UNIVERSITAS INTERNASIONAL")
    screen43.geometry("1280x720")
    screen43.resizable(0, 0)

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen43,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen43,text="Hasil Presensi Mata Kuliah Biologi",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    TableMargin = Frame(screen43, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Nama Lengkap", "NIM", "Kehadiran"),
                        height=300, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Nama Lengkap', text="Nama Lengkap", anchor=W)
    tree.heading('NIM', text="NIM", anchor=W)
    tree.heading('Kehadiran', text="Kehadiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    save_path = "Bio"
    namafile = os.path.join(save_path, f'{mmb1.get()}.csv')
    with open(namafile,'r', newline='\n') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            NamaLengkap = row['Nama']
            nim = row['NIM']
            Kehadiran = row['Kehadiran']
            tree.insert("", 0, values=(NamaLengkap, nim, Kehadiran))
    screen43.mainloop()

def menumahasiswa():
    global screen6
    screen6=Toplevel(screen)
    screen6.geometry("1280x720")
    screen6.title("Menu Mahasiswa")

    screen10_bg=PhotoImage(file="kotak.png")
    bgscreen10=Label(screen6,image=screen10_bg,bg="white")
    bgscreen10.place(x=0,y=0)

    title=Label(screen6,text="MATA KULIAH",bg="black",fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)
    
    Button(screen6,text="PROGRAMA KOMPUTER", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=prokom).place(x=20,y=170)
    Button(screen6,text="KALKULUS", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=kalkulus).place(x=430,y=170)
    Button(screen6,text="FISIKA DASAR II", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=fisdas).place(x=835,y=170)
    Button(screen6,text="ANALISIS & ESTIMASI BIAYA", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=AEB).place(x=20,y=320)
    Button(screen6,text="MATERIAL TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mattek).place(x=430,y=320)
    Button(screen6,text="MEKANIKA TEKNIK", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=mekatek).place(x=835,y=320)
    Button(screen6,text="PENGANTAR REKAYASA & DESAIN", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=PRD).place(x=20,y=470)
    Button(screen6,text="PSIKOLOGI INDUSTRI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=psikin).place(x=430,y=470)
    Button(screen6,text="BIOLOGI", width=30, height=5,font=("times new rommon",16,"bold"),relief=RIDGE,bd=7,command=bio).place(x=835,y=470)

    screen6.mainloop()
def kalkulus():
    global cmb3
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb3=ttk.Combobox(frame,value=course,width=15)
    cmb3.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisikalkulus).place(x=35,y=254) 
    cmb3.current(0)

    root.mainloop()

def AEB():
    global cmb
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb=ttk.Combobox(frame,value=course,width=15)
    cmb.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisiaeb).place(x=35,y=254) 
    cmb.current(0)


def PRD():
    global cmb6
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb6=ttk.Combobox(frame,value=course,width=15)
    cmb6.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisiprd).place(x=35,y=254) 
    cmb6.current(0)

    root.mainloop()
def psikin():
    global cmb8
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb8=ttk.Combobox(frame,value=course,width=15)
    cmb8.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisipsikin).place(x=35,y=254) 
    cmb8.current(0)

    root.mainloop()

def mekatek():
    global cmb5
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb5=ttk.Combobox(frame,value=course,width=15)
    cmb5.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisimekatek).place(x=35,y=254) 
    cmb5.current(0)

    root.mainloop()
def mattek():
    global cmb4
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb4=ttk.Combobox(frame,value=course,width=15)
    cmb4.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisimattek).place(x=35,y=254) 
    cmb4.current(0)

    root.mainloop()    
def fisdas():
    global cmb2
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb2=ttk.Combobox(frame,value=course,width=15)
    cmb2.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisifisdas).place(x=35,y=254) 
    cmb2.current(0)

    root.mainloop()
def bio():
    global cmb1
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb1=ttk.Combobox(frame,value=course,width=15)
    cmb1.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisibio).place(x=35,y=254) 
    cmb1.current(0)

    root.mainloop()    
def prokom():
    global cmb7
    root=Tk()
    root.title("SSO UNIVERSITAS INTERNASIONAL")
    root.geometry("1280x720")
    root.configure(bg="white")

    frame=Frame(root,width=360,height=350,bg="white")
    frame.place(x=480,y=70)

    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5","Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10","Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15"]
    heading=Label(frame,text="PILIH PERTEMUAN",fg="black",bg="white",font=("Acumin Variable Concept",20,"bold"))
    heading.place(x=52,y=25)
    cmb7=ttk.Combobox(frame,value=course,width=15)
    cmb7.place(x=125,y=100)
    Button(frame,width=40,pady=7,text="SUBMIT",bg="#57a1f8",fg="black",border=0, command=mengisiprokom).place(x=35,y=254) 
    cmb7.current(0)

    root.mainloop()

def mengisiaeb():
    global namalengkapentry,nimentry,combo_hadir
    screen17=Toplevel(screen)
    screen17.geometry("1280x720")
    screen17.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen17,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen17, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir["value"]=("Hadir","Sakit","Izin")
    combo_hadir.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvaeb,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen17, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()

def csvaeb():
    save_path = 'AEB'


    namafile = os.path.join(save_path, f'{cmb.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry.get(), 'NIM': nimentry.get(), 'Kehadiran': combo_hadir.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)
    
def mengisibio():
    global namalengkapentry1,nimentry1,combo_hadir1
    screen18=Toplevel(screen)
    screen18.geometry("1280x720")
    screen18.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen18,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen18, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry1=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry1.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry1=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry1.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir1=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir1["value"]=("Hadir","Sakit","Izin")
    combo_hadir1.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvbio,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen18, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
    

def csvbio():
    save_path = 'Bio'

    namafile = os.path.join(save_path, f'{cmb1.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry1.get(), 'NIM': nimentry1.get(), 'Kehadiran': combo_hadir1.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)
        
def mengisifisdas():
    global namalengkapentry2,nimentry2,combo_hadir2
    screen19=Toplevel(screen)
    screen19.geometry("1280x720")
    screen19.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen19,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen19, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry2=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry2.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry2=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry2.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir2=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir2["value"]=("Hadir","Sakit","Izin")
    combo_hadir2.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvfisdas,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen19, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvfisdas():
    save_path = 'Fisdas'

    namafile = os.path.join(save_path, f'{cmb2.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry2.get(), 'NIM': nimentry2.get(), 'Kehadiran': combo_hadir2.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

def mengisikalkulus():
    global namalengkapentry3,nimentry3,combo_hadir3
    screen20=Toplevel(screen)
    screen20.geometry("1280x720")
    screen20.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen20,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen20, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry3=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry3.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry3=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry3.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir3=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir3["value"]=("Hadir","Sakit","Izin")
    combo_hadir3.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvkalkulus,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen20, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvkalkulus():
    save_path = 'Kalkulus'

    namafile = os.path.join(save_path, f'{cmb3.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry3.get(), 'NIM': nimentry3.get(), 'Kehadiran': combo_hadir3.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

def mengisimattek():
    global namalengkapentry4,nimentry4,combo_hadir4
    screen21=Toplevel(screen)
    screen21.geometry("1280x720")
    screen21.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen21,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen21, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry4=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry4.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry4=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry4.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir4=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir4["value"]=("Hadir","Sakit","Izin")
    combo_hadir4.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvmattek,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen21, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvmattek():
    save_path = 'Mattek'

    namafile = os.path.join(save_path, f'{cmb4.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry4.get(), 'NIM': nimentry4.get(), 'Kehadiran': combo_hadir4.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

def mengisimekatek():
    global namalengkapentry5,nimentry5,combo_hadir5
    screen22=Toplevel(screen)
    screen22.geometry("1280x720")
    screen22.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen22,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen22, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry5=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry5.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry5=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry5.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir5=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir5["value"]=("Hadir","Sakit","Izin")
    combo_hadir5.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvmekatek,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen22, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvmekatek():
    save_path = 'Mekatek'

    namafile = os.path.join(save_path, f'{cmb5.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry5.get(), 'NIM': nimentry5.get(), 'Kehadiran': combo_hadir5.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

def mengisiprd():
    global namalengkapentry6,nimentry6,combo_hadir6
    screen23=Toplevel(screen)
    screen23.geometry("1280x720")
    screen23.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen23,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen23, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry6=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry6.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry6=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry6.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir6=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir6["value"]=("Hadir","Sakit","Izin")
    combo_hadir6.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvprd,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen23, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvprd():
    save_path = 'PRD'

    namafile = os.path.join(save_path, f'{cmb6.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry6.get(), 'NIM': nimentry6.get(), 'Kehadiran': combo_hadir6.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)
    
def mengisiprokom():
    global namalengkapentry7,nimentry7,combo_hadir7
    screen24=Toplevel(screen)
    screen24.geometry("1280x720")
    screen24.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen24,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen24, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry7=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry7.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry7=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry7.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir7=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir7["value"]=("Hadir","Sakit","Izin")
    combo_hadir7.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvprokom,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen24, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvprokom():
    save_path = 'Prokom'

    namafile = os.path.join(save_path, f'{cmb7.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry7.get(), 'NIM': nimentry7.get(), 'Kehadiran': combo_hadir7.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

def mengisipsikin():
    global namalengkapentry8,nimentry8,combo_hadir8
    screen25=Toplevel(screen)
    screen25.geometry("1280x720")
    screen25.title("Mengisi Presensi")
    bg_color="#c4c4bc"

    #======================Heading============#
    title=Label(screen25,text="PRESENSI MATA KULIAH",bg=bg_color,fg="black",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
    title.pack(fill=X)

    #====================Left frame============#
    F1=Frame(screen25, bg=bg_color, relief=RIDGE, bd=15)
    F1.place(x=10,y=80,width=650,height=530)

    nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nama.grid(row=0,column=0,padx=30,pady=10, sticky="w")
    namalengkapentry8=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    namalengkapentry8.grid(row=0,column=1, pady=10, sticky="w")

    nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    nim.grid(row=1,column=0,padx=30,pady=10,sticky="w")
    nimentry8=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
    nimentry8.grid(row=1,column=1, pady=10, sticky="w")

    hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
    hadir.grid(row=2,column=0,padx=30,pady=10,sticky="w")

    combo_hadir8=ttk.Combobox(F1,font=("times new rommon",18,"bold"),state="readonly")
    combo_hadir8["value"]=("Hadir","Sakit","Izin")
    combo_hadir8.grid(row=2,column=1,pady=10,sticky="w")

    Button(F1,width=40,pady=7,text="SUBMIT",bg=bg_color,command=csvpsikin,fg="black",font=("times new rommon",10,"bold"),relief=GROOVE,bd=11).grid(row=4,column=1, pady=10)

    #====================Right frame============#
    F2=Frame(screen25, bg="white")
    F2.place(x=665,y=80,width=610,height=530)

    bgdosen=PhotoImage(file="logoui.png")
    backgroundosen=Label(F2,image=bgdosen,bg="white")
    backgroundosen.place(x=45,y=0)

    F2.mainloop()
def csvpsikin():
    save_path = 'Psikin'

    namafile = os.path.join(save_path, f'{cmb8.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran']    

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': namalengkapentry8.get(), 'NIM': nimentry8.get(), 'Kehadiran': combo_hadir8.get()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
    
        writer.writerow(presensi)

main_screen()