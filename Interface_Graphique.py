from tkinter import *
import random
import subprocess
from tkinter.messagebox import showinfo
#lire le dictionnaire
with open("liste_de_mots_francais.txt", encoding='utf8') as fichier:
    texte = fichier.read()

#listes pour les lettres intredites
#sans le \n pour la proba que une lettre commence un mot
interdit_1er_niveau = ['-','é','è','à','ù','â','ô','ï','ö']
# on rajoute le \n
interdit_2eme_niveau = ['-','\n','é','è','à','ù','â','ô','ï','ö']

#definition des variables
lettre_pré = '\n'
lettre_pré_pré = '\n'
lettres = []
lettres_suiv = [[]]
lettres_suiv_suiv = [[]]

#
def ajout_lettre_dans_lettres(lettre_aj):
    if lettre_aj in interdit_1er_niveau:
        return None
    if lettre_aj not in lettres:
        lettres.append(lettre_aj)
        lettres_suiv.append([])
        lettres_suiv_suiv.append([])
    return lettres.index(lettre_aj)

def ajout_lettre_dans_lettre_suiv(lettre,index):
    if lettre in interdit_2eme_niveau:
        return None
    lettres_suiv[index].append(lettre)
    
def ajout_lettre_dans_lettre_suiv_suiv(lettre,index):
    if lettre in interdit_2eme_niveau:
        return None
    lettres_suiv_suiv[index].append(lettre)

for iLettre in range(len(texte)):
    lettre = texte[iLettre]
    if lettre == '\n':
        lettre_pré = '\n'
        lettre_pré_pré = '\n'
    index = ajout_lettre_dans_lettres(lettre_pré)
    if index != None:
        ajout_lettre_dans_lettre_suiv(lettre,index)
    index = ajout_lettre_dans_lettres(lettre_pré_pré)
    if index != None:
        ajout_lettre_dans_lettre_suiv_suiv(lettre,index)
    lettre_pré_pré = lettre_pré
    lettre_pré = lettre


def lettre_apres(mot):
    if mot == '':
        derniere_lettre = '\n'
    else:
        derniere_lettre = mot[len(mot)-1]
    index_derniere_lettre = lettres.index(derniere_lettre)
    if len(mot) >= 2:
        avant_derniere_lettre = mot[len(mot)-2]
        index_avant_dernière_lettre = lettres.index(avant_derniere_lettre)
        common = set(lettres_suiv[index_derniere_lettre]).intersection(lettres_suiv_suiv[index_avant_dernière_lettre])
        common = list(common)
        if len(common) <= 0:
            return None
        index_resultat = random.randint(0,len(common)-1)
        lettre = common[index_resultat]
    else:
        index_resultat = random.randint(0,len(lettres_suiv[index_derniere_lettre]))
        lettre = lettres_suiv[index_derniere_lettre][index_resultat]
    return lettre

def generer_mdp(long):
    if long > 12:
        return None
    if long < 4:
        return None
    mdp = ''
    for _ in range(long):
        mdp = mdp + lettre_apres(mdp)
    return mdp

def test():
    for iTest in range(100):
        generer_mdp(780)
    return('Tout va bien')

def generer_mdp_pls_mots(long,nbs_de_mots):
    mdp_pls_mots = str(generer_mdp(long))
    for iMdp in range(nbs_de_mots - 1):
        mdp_pls_mots = mdp_pls_mots + '-' + str(generer_mdp(long))
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

    mdp_gen = generer_mdp_pls_mots(int(nb_lettres.get()),int(nb_mots.get()))
    Label(fenetre, text=mdp_gen).pack(padx=10, pady=10)

def copier():
    process = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
    process.communicate(bytes(mdp_gen, 'utf-8'))

Canvas(fenetre, width=250, height=100, bg='ivory').pack(side=TOP, padx=5, pady=5)
bouton_creer = Button(fenetre, text ='Créer', command=creer).pack(side=LEFT, padx=5, pady=5)
Button(fenetre, text ='Copier', command=copier).pack(side=RIGHT, padx=5, pady=5)

fenetre.mainloop()
