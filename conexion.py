
#page de connexion
from subprocess import call
from tkinter import *
from tkinter import ttk
import customtkinter
from PIL import Image,ImageTk
# import mysql.connector as mysql
# import  os
# from tkinter import messagebox



    #fenetre pricipale
fenetre1=Tk()
fenetre1.geometry("1000x620")
fenetre1.resizable(False, False)
fenetre1.title("page de connexion")

def cpte():
    fenetre1.destroy()
    call(["python", "creercompte.py"])

    # cacher mot de passe
def cachermdp():
    if champ1.cget('show')=='':
        champ1.config(show='*')
        bt_affiche.config(image=image2)
    else:
        champ1.config(show='')
        bt_affiche.config(image=image1)

    #cadre pricipale

photo=ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))
x=Label(fenetre1,image=photo)
x.place(x='',y='')
x.pack()

cadre=Frame(fenetre1,bg="#ffffff",width=500,height=350)

texte=Label (cadre,text="Connexion",font=('Calistoga',25),bg="white")
texte.place(x=180,y=40,)



texte=Label (cadre,text="Email",font=('Calistoga',13),bg="white")
texte.place(x='70',y=110)
champ=Entry(cadre,bg="#ffffff",width=25,font=('Calistoga',20))
champ.place(x=60,y=140,)

texte = Label(cadre, text="Mot de passe", font=('Calistoga', 13), bg="white")
texte.place(x=70, y=190)
champ1 = Entry(cadre, bg="white", width=25, show="*", font=('Calistoga', 20))
champ1.place(x=60, y=220)


image1=PhotoImage(file="C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\ouvert2.png")
x=Label(cadre,image=image1)
image2=PhotoImage(file="C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\ferme2.png")
y=Label(fenetre1,image=image2)

bt_affiche=Button(cadre,command=cachermdp,image=image1,width=30,height=30)
bt_affiche.place(x=400,y=220)


but= customtkinter.CTkButton(master=cadre,text="Se connecter",text_font=('Calistoga',15),command=quit,
                                      height=30,width=360,border_width=1,corner_radius=10,fg_color="#319BFE")
but.place(x=70,y=270)

pad= customtkinter.CTkButton(master=cadre,text="Créer un compte",text_font=('Italic',11),command=cpte,
                                      height=20,width=200,border_width=0,corner_radius=10,fg_color="white",text_color="black")
pad.place(x=150,y=310)

cadre.place(relx=0.5, rely=0.5, anchor=CENTER)
#     #cadre.pack(padx=20, pady=20)

# def admin():
#     fenetre1.destroy()
#     # call(["python","conexion.py"])
#     #import creercompte
#
#
# fenetre1.after(1500, admin)

fenetre1.mainloop()