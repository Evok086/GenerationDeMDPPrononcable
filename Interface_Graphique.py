from tkinter import * 

fenetre = Tk()

label = Label(fenetre, text="Combien de Mots ?")
label.pack()

# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="1", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="2", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="3", variable=value, value=3)
bouton4 = Radiobutton(fenetre, text="4", variable=value, value=4)
bouton5 = Radiobutton(fenetre, text="5", variable=value, value=5)
bouton6 = Radiobutton(fenetre, text="6", variable=value, value=6)
bouton1.pack()
bouton2.pack()
bouton3.pack()
bouton4.pack()
bouton5.pack()
bouton6.pack()

label = Label(fenetre, text="Combien de Lettres ?")
label.pack()

s = Spinbox(fenetre, from_=4, to=12)
s.pack()

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
Button(fenetre, text ='Créer').pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Copier').pack(side=RIGHT, padx=5, pady=5)

fenetre.mainloop()