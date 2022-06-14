from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color

root=Tk()
root.title("Melihat Presensi")
root.geometry("1280x720")
bg_color="#990099"

#======================Heading============#
title=Label(root,text="PRESENSI MATA KULIAH",bg=bg_color,fg="white",font=("times new rommon",35,"bold"),relief=GROOVE,bd=12)
title.pack(fill=X)

#====================Left frame============#
F1=Frame(root, bg=bg_color, relief=RIDGE, bd=15)
F1.place(x=10,y=80,width=650,height=530)

nama=Label(F1,text="Nama Lengkap",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
nama.grid(row=0,column=0,padx=30,pady=10)
namalengkapentry=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
namalengkapentry.grid(row=0,column=1, pady=10, sticky="w")

nim=Label(F1,text="NIM",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
nim.grid(row=1,column=0,padx=30,pady=10)
nimentry=Entry(F1,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
nimentry.grid(row=1,column=1, pady=10, sticky="w")

hadir=Label(F1,text="Kehadiran",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
hadir.grid(row=2,column=0,padx=30,pady=10)

combo_hadir=ttk.Combobox(F1,font=("times new rommon",20,"bold"),state="readonly")
combo_hadir["value"]=("Hadir","Sakit","Izin")
combo_hadir.grid(row=2,column=1,pady=10)

keterangan=Label(F1,text="Keterangan",font=("times new rommon",20,"bold"),fg="black",bg=bg_color)
keterangan.grid(row=3,column=0,padx=30,pady=10)
keteranganentry=Text(F1,width=20,height=3,font=("times new rommon",18,"bold"),relief=RIDGE,bd=7)
keteranganentry.grid(row=3,column=1, pady=10, sticky="w")

#====================Right frame============#
F1=Frame(root, bg=bg_color, relief=RIDGE, bd=15)
F1.place(x=665,y=80,width=610,height=530)



root.mainloop()