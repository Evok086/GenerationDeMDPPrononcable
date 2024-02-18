import random
with open("liste_de_mots_francais.txt", encoding='utf8') as fichier:
    texte = fichier.read()
    

lettres = []
interdit_1er_niveau = ['-']
interdit_2eme_niveau = ['-','\n']

lettre_pré = '\n'
lettres_suiv = []
for i in range(len(texte)):
    lettre = texte[i]
    if lettre_pré not in interdit_1er_niveau:
        if lettre_pré not in lettres:
            lettres.append(lettre_pré)
            if lettre not in interdit_2eme_niveau:
                lettres_suiv.append([lettre])
            else:
                lettres_suiv.append([])
        else:
            if lettre not in interdit_2eme_niveau:
                index = lettres.index(lettre_pré)
                lettres_suiv[index].append(lettre)
    lettre_pré = lettre

def lettre_apres(mot):
    if mot == '':
        derniere_lettre = '\n'
    else:
        derniere_lettre = mot[len(mot)-1]
    index = lettres.index(derniere_lettre)
    i = random.randint(0,len(lettres_suiv[index]))
    letter = lettres_suiv[index][i]
    return letter

'''def lettre_apres(letter):
    #Cette fonction consiste à donner une lettre aléatoire qui a une probabilité d'arriver après la lettre entrée sauf les espaces et les caractères spéciaux
    j = 0
    i = random.randint(0, 1866720)
    condition = False
    while j == 0 :
        i = i + 1
        if letter == 's' or letter == 't' or letter == 'r' or letter == 'l':
            condition = texte[i+1]=='s' or texte[i+1]=='t' or texte[i+1]=='r' or texte[i+1]=='l'
        if letter == 'i':
            condition = texte[i+1]=='e'
        if letter == 'e':
            condition = texte[i+1]=='a'
        if texte[i]==letter and not(texte[i+1]=='\n' or texte[i+1]==' ' or texte[i+1]=='-' or texte[i+1]=='é' or texte[i+1]=='à' or texte[i+1]=='ç' or texte[i+1]=='ù' or texte[i+1]=='î' or texte[i+1]=='ê' or texte[i+1]=='è' or texte[i+1]=='â' or condition) :
            j = 1
            return texte[i+1]'''

def mdp(long):
    mdp = ''
    for _ in range(long):
        mdp = mdp + lettre_apres(mdp)
    return mdp

def test():
    for i in range(100):
        mdp(780)
    return('Tout va bien')

def mdp_pls_mots(long,nbs_de_mots):
    mdp_pls_mots = str(mdp(long))
    for i in range(nbs_de_mots - 1):
        mdp_pls_mots = mdp_pls_mots + '-' + str(mdp(long))
    return mdp_pls_mots
    
