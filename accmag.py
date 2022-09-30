

# page acceuil mag
from subprocess import call
from tkinter import *
from tkinter import ttk

import customtkinter as customtkinter
from PIL import Image, ImageTk


# import mysql.connector
# from tkinter import mess



fenetre3 = Tk()
fenetre3.title("page d'acceil Admin")
fenetre3.geometry("1000x620")
fenetre3.resizable(False, False)
fenetre3.configure(bg="white")

def produit():
    fenetre3.destroy()
    call(["python", "prodmag.py"])


def retour():
    fenetre3.destroy()
    call(["python", "accmag.py"])


def prod():
    fenetre3.destroy()
    call(["python", "prodmag.py"])


def four():
    fenetre3.destroy()
    call(["python", "fourmag.py"])


def vente():
    fenetre3.destroy()
    call(["python", "ventes.py"])


def deconnexion():
    fenetre3.destroy()
    call(["python", "conexion.py"])

# corps
fram = Frame(fenetre3, bg='#FFFFFF', width='1000', height='250')
fram.place(x='', y='')

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))
x = Label(fram, image=photo)
x.place(x='0', y='')

Label(master=fram, text="Accueil",font=('Calistoga', 30),
                                 fg='#319BFE').place(x='10', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Produits", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=prod)
bouton.place(x='180', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Vente", text_font=('Calistoga', 20), width=170, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=vente)
bouton.place(x='360', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Fournisseur", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=four)
bouton.place(x='570', y='170')
bouton = customtkinter.CTkButton(master=fram, text="Deconnexion", text_font=('Calistoga', 20), width=100, height=20,
                                 fg_color='#319BFE',corner_radius=15, border_width=1, command=deconnexion)
bouton.place(x='800', y='170')
# recherche
logo = Label(fram, text="Bienvenue Magasinier!!!", font=('Italic', 30))
logo.place(x="550", y="10")
# logo
logo = Label(fram, text=" BIGSTOCK", font=('Italic', 30))
logo.place(x="10", y="10")

fram0 = Frame(fenetre3, width='1000', height='370')
fram0.place(x='', y='250')

# logo=PhotoImage(file=r"BIG STOCK1.png")
# img=Button( image=logo).place(x=10,y=20)
prod0 = Button(fram0, text="Total Produits\n      104", bg="#319BFE", command=quit, fg="white", font=('', 25,),
               width="15", height="3")
prod0.place(x="10", y="80")
prod1 = Button(fram0, text="Total Magasiniers\n     3", bg="#319BFE", command=quit, fg="white", font=('', 25,),
               width="15", height="3")
prod1.place(x="350", y="80")
prod2 = Button(fram0, text="Total Fournisseurs\n       15 ", bg="#319BFE", fg="white", command=quit, font=('', 25,),
               width="15", height="3")
prod2.place(x="700", y="80")

# copyrith
preven = Label(fenetre3, text="Copyright @ 0101 par Groupe 2/ODC", font=("Arial", 10))
preven.place(x="350", y="600")


def admin():
    fenetre3.destroy()
    # call(["python","conexion.py"])
    #import accmag



fenetre3.mainloop()
