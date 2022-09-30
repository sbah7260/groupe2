from subprocess import call
from tkinter import *
from tkinter import Entry
from tkinter import ttk
from PIL import Image, ImageTk


def retour():
    fenetre7.destroy()
    call(["python", "accadmin.py"])


fenetre7 = Tk()
fenetre7.title("Les produits Admin ")
fenetre7.geometry("1000x620")
fenetre7.resizable(False, False)
fenetre7.configure(bg="white")

bg = ImageTk.PhotoImage(Image.open("C:\\Users\\BAH\\PycharmProjects\\HelloWorld\\image4.png"))
x = Label(fenetre7, image=bg)
x.place(x='', y='')
x.pack()

texte = Label(fenetre7, text="Les Produits", font=('Calistoga', 25), bg="#68B1F3")
texte.place(x=400, y=30, )
ret = Button(fenetre7, text="<<Retour", font=('Calistoga', 8), bg="white", command=retour)
ret.place(x=5, y=30, )

# champ de recherche
texte = Label(fenetre7, text="Recherche", font=('Calistoga', 13), bg="#A79292")
texte.place(x=20, y=150)
champ1 = Entry(fenetre7, bg="white", width=25, show="*", font=('Calistoga', 15))
champ1.place(x=140, y=150)

# affichage resultat
aff = ttk.Treeview(fenetre7, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
aff.place(x='140', y='200', width=800, height=350)

# nouveau fonction

"""def afficher():

    con = pymysql.connect(host="localhost", user="root", password="", database="bigstock")
    cursor=con.cursor()
    cursor.execute("select * from produit ")
    aff.delete(*aff.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id,nom,quantite,date_arrive,fournisseur,telephone) in enumerate (records,start=1):
            aff.insert ("", "end", values=(id,nom,quantite,date_arrive,fournisseur,telephone))

    con.close()"""

# en tete
aff.heading(1, text="ID")
aff.heading(2, text="Nom")
aff.heading(3, text="Quantité")
aff.heading(4, text="Date d'arrivée")
aff.heading(5, text="Fournisseur")
aff.heading(6, text="Télephone Founisseur")
# dimension des colonnes
aff.column(1, width=10)
aff.column(2, width=10)
aff.column(3, width=10)
aff.column(4, width=10)
aff.column(5, width=10)
aff.column(6, width=10)

# suivante et precedente
pad = Button(master=fenetre7, text="<<Précedente", font=('Calistoga', 11), command=quit, fg="#000000",
             width=11, bg="#ffffff")
pad.place(x=690, y=565)

pad = Button(master=fenetre7, text="Suivante>>", font=('Calistoga', 11), command=quit, fg="#000000",
             width=10, bg="#ffffff")
pad.place(x=840, y=565)

fenetre7.mainloop()
