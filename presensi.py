import tkinter as Tk
from tkinter import *
from turtle import Screen, bgcolor
from tkinter import ttk
import tkinter.messagebox
import os
import csv
import pandas as pd

def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250")
    screen.title("Presensi Mahasiswa")
    Label(text="Selamat datang di website presensi Universitas Sorong", bg="green", width="300", height="2", font=("comic sans",12)).pack()
    Label(text="").pack()
    Button(text="Mahasiswa", bg="grey", width="30", height="2", command=mahasiswa_login).pack()
    Label(text="").pack()
    Button(text="Dosen", bg="grey", width="30", height="2", command=dosen_login).pack()
    Label(text="").pack()
   
    screen.mainloop()

def mahasiswa_login():
    global screen2,nimmahasiswa,namamahasiswa,labelhasil
    screen2=Toplevel(screen)
    screen2.title("Login Mahasiswa")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    Label(screen2, text="Nama Lengkap").pack()
    namamahasiswa=Entry(screen2) #textvariable=login)
    namamahasiswa.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="NIM").pack()
    nimmahasiswa=Entry(screen2) #textvariable=password_verify)
    nimmahasiswa.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=loginmahasiswa_verify).pack()

    labelhasil=Label(screen2)
    labelhasil.pack()

    namamahasiswa.delete(0,END)
    nimmahasiswa.delete(0,END)

def dosen_login():
    global screen3,labeldosen,namadosen,niddosen
    screen3=Toplevel(screen)
    screen3.title("Login Dosen")
    screen3.geometry("300x250")
    Label(screen3, text="Please enter details below to login").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Nama Lengkap").pack()
    namadosen=Entry(screen3) #textvariable=)
    namadosen.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="NID").pack()
    niddosen=Entry(screen3) #textvariable=)
    niddosen.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Login", width=10, height=1, command=logindosen_verify).pack()

    labeldosen=Label(screen3)
    labeldosen.pack()

def loginmahasiswa_verify():
    userData = pd.read_csv('datamahasiswa.csv')
    df = pd.DataFrame(userData)

    inputnama = namamahasiswa.get().upper()
    inputnim = nimmahasiswa.get().upper()

    mc = (len(df[(df.Nama_Lengkap == inputnama) & (df.NIM == inputnim)]) > 0)
    if mc:
        labelhasil.configure(text="Berhasil")
        menumahasiswa()
    else:
       labelhasil.configure(text="Gagal")

def logindosen_verify():
    userData = pd.read_csv('datadosen.csv')
    df = pd.DataFrame(userData)

    inputdosen = namadosen.get().capitalize()
    inputnid = niddosen.get().capitalize()

    mc = (len(df[(df.Nama_dosen == inputdosen) & (df.NID == inputnid)]) > 0)
    if mc:
        labeldosen.configure(text="Sukses")
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