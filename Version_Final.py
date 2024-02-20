from tkinter import *
import random
import subprocess
with open("liste_de_mots_francais.txt", encoding='utf8') as fichier:
    texte = fichier.read()
    
def lettre_apres(letter):
    '''Cette fonction consiste à donner une lettre aléatoire qui a une probabilité d'arriver après la lettre entrée sauf les espaces et les caractères spéciaux'''
    #Cette fonction utilise une valeur aléatoire et parcoure la variable 'texte' afin de rechercher la lettre rentré par l'utilisateur
    j = 0
    i = random.randint(0, 1866720) #Valeur aléatoire
    condition = False
    while j == 0 :
        i = i + 1
        #Liste de Condition 
        if letter == 's' or letter == 'n' or letter == 't' or letter == 'r' or letter == 'p' or letter == 'c' or letter == 'l' or letter == 'd':
            condition = texte[i+1]=='s' or texte[i+1]=='t' or texte[i+1]=='r' or texte[i+1]=='n' or texte[i+1]=='p' or texte[i+1]=='c' or texte[i+1]=='l' or texte[i+1]=='d'
        if letter == 'i':
            condition = texte[i+1]=='e'
        if letter == 'e':
            condition = texte[i+1]=='a'
        if letter == 'w':
            condition = texte[i+1]=='n' or texte[i+1]=='s' or texte[i+1]=='b'
        if letter == 'f':
            condition = texte[i+1]=='s' or texte[i+1]=='f'
        if letter == 'k':
            condition = texte[i+1]=='f'
        if texte[i]==letter and ord(texte[i+1])<122 and ord(texte[i+1])>97 and not(texte[i+1]=='\n' or condition) :
            j = 1
            return texte[i+1] #Retourner la valeur aléatoire suivant la lettre rentrée par l'utilisateur
            
def mdp(long):
    mdp = chr(random.randint(97, 122)) #Première lettre
    for _ in range(long-1):
        mdp = mdp + lettre_apres(mdp[len(mdp)-1]) #Génération du mot de passe
    return mdp

#Fonction de test (crash-test), cette fonction s'éxecute en environ une minute
def test():
    for i in range(100):
        mdp(780)
    return('Tout va bien')

def mdp_pls_mots(long,nbs_de_mots):
    mdp_pls_mots = str(mdp(long)) #Premier Mot
    for i in range(nbs_de_mots - 1):
        mdp_pls_mots = mdp_pls_mots + '-' + str(mdp(long)) #Génération des mots de passes séparé par un tirêt
    return mdp_pls_mots

fenetre = Tk()

fenetre.title("Génération de MdP")

label = Label(fenetre, text="Combien de Mots ?")
label.pack()

nb_mots = Spinbox(fenetre, from_=1, to=6)
nb_mots.pack()

label = Label(fenetre, text="Combien de Lettres ?")
label.pack()

nb_lettres = Spinbox(fenetre, from_=4, to=12)
nb_lettres.pack()

zone_mdp = Label(fenetre).pack(padx=10, pady=10)
mdp_gen = ''

def creer(): 
    mdp_gen = mdp_pls_mots(int(nb_lettres.get()),int(nb_mots.get()))
    Label(fenetre,text=mdp_gen).pack(padx=10, pady=10)

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
bouton_creer = Button(fenetre, text ='Créer', command=creer).pack(side=LEFT, padx=5, pady=5)

fenetre.mainloop()
