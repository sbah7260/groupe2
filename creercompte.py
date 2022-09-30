from tkinter import *
import tkinter.messagebox as messageBox
from PIL import Image, ImageTk
import customtkinter
import mysql.connector as mysql

from subprocess import call

root = Tk()
root.title("Créer un compte")

root.geometry("1000x620")


def ajouter():
    id = idchamp.get()
    nom = nomchamp.get()
    prenom = prenomchamp.get()
    telephone = telechamp.get()
    email = emailchamp.get()
    modpas = modpaschamp.get()

    if (nom == "" or prenom == "" or telephone == "" or email == "" or modpas == ""):
        messageBox.showinfo("Echec", "Tous les champs sont requis")

    elif (modpaschamp.get() != rmdpchamp.get()):
        messageBox.showinfo("Echec", "Les deux mot de passe sont différentes veuille revoir")
    else:
        con = mysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute \
            ("insert into admin values('" + id + "','" + nom + "','" + prenom + "','" + telephone + "','" + email + "','" + modpas + "') ")
        cursor.execute("commit")

        idchamp.delete(0, "end")
        nomchamp.delete(0, "end")
        prenomchamp.delete(0, "end")
        telechamp.delete(0, "end")
        emailchamp.delete(0, "end")
        modpaschamp.delete(0, "end")
        rmdpchamp.delete(0, "end")

        con.close()


def clik():
    id = idchamp.get()
    nom = nomchamp.get()
    prenom = prenomchamp.get()
    telephone = telechamp.get()
    email = emailchamp.get()
    modpas = modpaschamp.get()
    # adresse = adressechamp.get()
    # date_arr = datechamp.get()

    if idchamp == " " or nomchamp == " " or prenomchamp == " " or telechamp == " " or emailchamp == " " or modpaschamp == " ":
        messageBox.showinfo("Echec", "Tous les champs sont requis")

    elif modpaschamp.get() != rmdpchamp.get():
        messageBox.showinfo("Echec", "Les deux mot de passe sont différentes veuille revoir")

    elif v.get( ) == "Administrateur":

        con = mysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute(
            'insert into admin values(\'' + id + "','" + nom + "','" + prenom + "','" + telephone + "','" + email + "','" + modpas + "') ")
        cursor.execute("commit")

        idchamp.delete(0, "end")
        nomchamp.delete(0, "end")
        prenomchamp.delete(0, "end")
        telechamp.delete(0, "end")
        emailchamp.delete(0, "end")
        modpaschamp.delete(0, "end")
        rmdpchamp.delete(0, "end")
        messageBox.showinfo("Message", "Compte Adminstrateur crée avec succèes")


    elif v.get( ) == "Magasinier":

        con = mysql.connect(host="localhost", user="root", password="sidi", database="bigstock")
        cursor = con.cursor()
        cursor.execute(
            "insert into mag values('" + id + "','" + nom + "','" + prenom + "','" + telephone + "','" + email + "','" + modpas + "') ")
        cursor.execute("commit")

        idchamp.delete(0, "end")
        nomchamp.delete(0, "end")
        prenomchamp.delete(0, "end")
        telechamp.delete(0, "end")
        emailchamp.delete(0, "end")
        modpaschamp.delete(0, "end")
        rmdpchamp.delete(0, "end")
        messageBox.showinfo("Message", "Compte Magasinier crée avec succèes ")
        con.close()
    #
    else:
        messageBox.showinfo("message", "Bienvenue !!!")



photo = ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))

x = Label(root, image=photo)
x.place(x='', y='')
x.pack()

frame1 = Frame(root, bg="#ffffff", width=700, height=500)
frame1.place(relx=0.5, rely=0.5, anchor=CENTER)

t2 = Label(frame1, text="Créer un compte", font=('calistoga', 35), bg="#ffffff", fg="#000000").place(x=150, y=20)

id = Label(frame1, text="ID", bg="#ffffff", fg="#000000", font=("", 10)).place(x=70, y=120)
idchamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
idchamp.place(x=70, y=140, )


nom = Label(frame1, text="Nom", bg="#ffffff", fg="#000000", font=("", 10)).place(x=70, y=160)

nomchamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
nomchamp.place(x=70, y=180)

prenom = Label(frame1, text="Prénom", bg="#ffffff", fg="#000000", font=("", 10)).place(x=70, y=210)

prenomchamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
prenomchamp.place(x=70, y=230)

tele = Label(frame1, text="Téléphone", bg="#ffffff", fg="#000000", font=("", 10)).place(x=70, y=250)

telechamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
telechamp.place(x=70, y=280, )

email = Label(frame1, text="Email", bg="#ffffff", fg="#000000", font=("", 10)).place(x=360, y=120)

emailchamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
emailchamp.place(x=360, y=140)

mdp = Label(frame1, text="Mot de passe", bg="#ffffff", fg="#000000", font=("", 10)).place(x=360, y=160)

modpaschamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
modpaschamp.place(x=360, y=180)

rmdp = Label(frame1, text="Répéter mot de passe", bg="#ffffff", fg="#000000", font=("", 10)).place(x=360, y=210)

rmdpchamp = Entry(frame1, bg="white", width=25, font=('Calistoga', 10))
rmdpchamp.place(x=360, y=230)

stt = Label(frame1, text="Statut", bg="#ffffff", fg="#000000", font=("", 10)).place(x=360, y=250)

v = StringVar()
v.set("Administrateur")  # initialiser
r1 = Radiobutton(frame1, text="Administrateur", variable=v, value="Administrateur", bg="#ffffff", fg="#000000",
                 font=("", 10),
                 command=lambda: clik())
r1.place(x=360, y=280)
r2 = Radiobutton(frame1, text="Magasinier", variable=v, value="Magasinier", bg="#ffffff", fg="#000000", font=("", 10),
                 command=lambda: clik())
r2.place(x=520, y=280)

label = Label(frame1)

pad = customtkinter.CTkButton(master=root, text="Valider", text_font=("Calistoga", 15), text_color="#ffffff",
                              height=30, width=200, border_width=1, corner_radius=10, fg_color="#319BFE",
                              command=ajouter)
pad.place(x=400, y=450)


root.mainloop()
