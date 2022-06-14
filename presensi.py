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
    #Button(screen4, text="Membuat Presensi", bg="grey", width="30", height="2", command=membuat_presensi)
    #Button(screen4, text="Melihat Presensi", bg="grey", width="30", height="2", command=melihat_presensi)
    screen4.mainloop()

def membuat_presensi():
    global screen5
    screen5=Toplevel(screen)
    screen5.geometry("1280x720")
    screen5.title("Membuat Presensi")
    Button(screen5, text="Programa Komputer", width="30", height="2", command=mprokom).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Kalkulus", width="30", height="2", command=mkalkulus).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Fisika Dasar", width="30", height="2", command=mfisdas).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Anggaran dan Estimasi Biaya", width="30", height="2", command=mAEB).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Material Teknik", width="30", height="2", command=mmattek).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Mekanika Teknik", width="30", height="2", command=mmekatek).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Pengantar Rekayasa dan Desain", width="30", height="2", command=mPRD).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Psikologi Industri", width="30", height="2", command=mpsikin).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="Biologi", width="30", height="2", command=mbio).pack()
    Label(screen5, text="").pack()


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
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Prokom"
    namafile = os.path.join(save_path, f'Pertemuan {defprokom.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None

        writer.writerow(presensi)
    
def mkalkulus():
    global screen10, defkalkulus
    screen10=Toplevel(screen)
    screen10.geometry("1280x720")
    screen10.title("Keterangan Pertemuan")
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Input Pertemuan").pack()
    defkalkulus=Entry(screen10)
    defkalkulus.pack()
    Label(screen10, text="").pack()
    Button(screen10, text="SUBMIT", width=10, height=1, command=savekalkulus).pack()

def savekalkulus():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Kalkulus"
    namafile = os.path.join(save_path, f'Pertemuan {defkalkulus.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mAEB():
    global screen11, defAEB
    screen11=Toplevel(screen)
    screen11.geometry("1280x720")
    screen11.title("Keterangan Pertemuan")
    Label(screen11, text="").pack()
    Label(screen11, text="").pack()
    Label(screen11, text="").pack()
    Label(screen11, text="Input Pertemuan").pack()
    defAEB=Entry(screen11)
    defAEB.pack()
    Label(screen11, text="").pack()
    Button(screen11, text="SUBMIT", width=11, height=1, command=saveAEB).pack()

def saveAEB():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\AEB"
    namafile = os.path.join(save_path, f'Pertemuan {defAEB.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mPRD():
    global screen12, defPRD
    screen12=Toplevel(screen)
    screen12.geometry("1280x720")
    screen12.title("Keterangan Pertemuan")
    Label(screen12, text="").pack()
    Label(screen12, text="").pack()
    Label(screen12, text="").pack()
    Label(screen12, text="Input Pertemuan").pack()
    defPRD=Entry(screen12)
    defPRD.pack()
    Label(screen12, text="").pack()
    Button(screen12, text="SUBMIT", width=12, height=1, command=savePRD).pack()

def savePRD():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\PRD"
    namafile = os.path.join(save_path, f'Pertemuan {defPRD.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mpsikin():
    global screen13, defpsikin
    screen13=Toplevel(screen)
    screen13.geometry("1280x720")
    screen13.title("Keterangan Pertemuan")
    Label(screen13, text="").pack()
    Label(screen13, text="").pack()
    Label(screen13, text="").pack()
    Label(screen13, text="Input Pertemuan").pack()
    defpsikin=Entry(screen13)
    defpsikin.pack()
    Label(screen13, text="").pack()
    Button(screen13, text="SUBMIT", width=13, height=1, command=savepsikin).pack()

def savepsikin():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Psikin"
    namafile = os.path.join(save_path, f'Pertemuan {defpsikin.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mmekatek():
    global screen14, defmekatek
    screen14=Toplevel(screen)
    screen14.geometry("1280x720")
    screen14.title("Keterangan Pertemuan")
    Label(screen14, text="").pack()
    Label(screen14, text="").pack()
    Label(screen14, text="").pack()
    Label(screen14, text="Input Pertemuan").pack()
    defmekatek=Entry(screen14)
    defmekatek.pack()
    Label(screen14, text="").pack()
    Button(screen14, text="SUBMIT", width=14, height=1, command=savemekatek).pack()

def savemekatek():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Mekatek"
    namafile = os.path.join(save_path, f'Pertemuan {defmekatek.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mmattek():
    global screen15, defmattek
    screen15=Toplevel(screen)
    screen15.geometry("1280x720")
    screen15.title("Keterangan Pertemuan")
    Label(screen15, text="").pack()
    Label(screen15, text="").pack()
    Label(screen15, text="").pack()
    Label(screen15, text="Input Pertemuan").pack()
    defmattek=Entry(screen15)
    defmattek.pack()
    Label(screen15, text="").pack()
    Button(screen15, text="SUBMIT", width=15, height=1, command=savemattek).pack()

def savemattek():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Mattek"
    namafile = os.path.join(save_path, f'Pertemuan {defmattek.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)


def mfisdas():
    global screen16, deffisdas
    screen16=Toplevel(screen)
    screen16.geometry("1280x720")
    screen16.title("Keterangan Pertemuan")
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Input Pertemuan").pack()
    deffisdas=Entry(screen16)
    deffisdas.pack()
    Label(screen16, text="").pack()
    Button(screen16, text="SUBMIT", width=16, height=1, command=savefisdas).pack()

def savefisdas():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Fisdas"
    namafile = os.path.join(save_path, f'Pertemuan {deffisdas.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)

def mbio():
    global screen16, defbio
    screen16=Toplevel(screen)
    screen16.geometry("1280x720")
    screen16.title("Keterangan Pertemuan")
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="").pack()
    Label(screen16, text="Input Pertemuan").pack()
    defbio=Entry(screen16)
    defbio.pack()
    Label(screen16, text="").pack()
    Button(screen16, text="SUBMIT", width=16, height=1, command=savebio).pack()

def savebio():
    global namafile, csvheader, writer, presensi
    #####------------------------------------------PENTING!!!!-----------------------------------------#####
    #####-----------------------------KALO MAU RUN SAVE_PATH DIUBAH DULU-----------------------------------------#####
    save_path = "D:\Kuliah\Tugas_Prokom_Praktikum\ABSENSI-MAHASISWA\Bio"
    namafile = os.path.join(save_path, f'Pertemuan {defbio.get()}.csv')
    csvheader = ['Nama', 'NIM', 'Kehadiran', 'Keterangan']

    #Membuka file csv dalam mode append
    with open(namafile,'a', newline='\n') as filecsv:

        #dictnilai adalah dictionary digunakan untuk writerow.
        #Mengubah data menjadi dictionary untuk dimasukkan per row
        presensi = {'Nama': print(), 'NIM': print(), 'Kehadiran': print(), 'Keterangan': print()}

        writer = csv.DictWriter(filecsv, fieldnames = csvheader)

        #Jika file tidak ada, maka auto membuat file dan menambah csvheader di dalamnya
        if os.stat(namafile).st_size == 0:
            writer.writeheader()
        else:
            None
            
        writer.writerow(presensi)

def Pertemuan1():
    print()

def Pertemuan2():
    print()

def Pertemuan3():
    print()

def Pertemuan4():
    print()

def Pertemuan5():
    print()

def Pertemuan6():
    print()

def Pertemuan7():
    print()

def Pertemuan8():
    print()

def Pertemuan9():
    print()

def Pertemuan10():
    print()

def Pertemuan11():
    print()

def Pertemuan12():
    print()

def Pertemuan13():
    print()

def Pertemuan14():
    print()

def Pertemuan15():
    print()

def Pertemuan16():
    print()

def melihat_presensi():
    global screen10
    screen10=Toplevel(screen)
    screen10.geometry("1280x720")
    screen10.title("Melihat Presensi")
    Button(screen10, text="Programa Komputer", width="30", height="2", command=prokom).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Kalkulus", width="30", height="2", command=kalkulus).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Fisika Dasar", width="30", height="2", command=fisdas).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Anggaran dan Estimasi Biaya", width="30", height="2", command=AEB).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Material Teknik", width="30", height="2", command=mattek).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Mekanika Teknik", width="30", height="2", command=mekatek).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Pengantar Rekayasa dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen10, text="").pack()


def menumahasiswa():
    global screen6
    screen6=Toplevel(screen)
    screen6.geometry("1280x720")
    screen6.title("Melakukan Presensi")
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
    Button(screen6, text="Pengantar Rekayasa dan Desain", width="30", height="2", command=PRD).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Psikologi Industri", width="30", height="2", command=psikin).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="Biologi", width="30", height="2", command=bio).pack()
    Label(screen6, text="").pack()

def kalkulus():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def AEB():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def PRD():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def psikin():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def mekatek():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def mattek():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def fisdas():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def bio():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def prokom():
    root=Tk()
    root.title("Melihat Presensi")
    root.geometry("1280x720")
    course=["Pertemuan 1", "Pertemuan 2", "Pertemuan 3", "Pertemuan 4", "Pertemuan 5", "Pertemuan 6", "Pertemuan 7", "Pertemuan 8", "Pertemuan 9", "Pertemuan 10", "Pertemuan 11", "Pertemuan 12", "Pertemuan 13", "Pertemuan 14", "Pertemuan 15", "Pertemuan 16"]
    l1=Label(root,text="Pilih pertemuan ke")
    l1.grid(row=0,column=0)
    cmb=ttk.Combobox(root,value=course,width=15)
    cmb.grid(row=16,column=16)
    cmb.current(0)
    root.mainloop()

def melihat_bio():
    print()


main_screen()