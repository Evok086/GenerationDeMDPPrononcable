import random
with open("liste_de_mots_francais.txt", encoding='utf8') as fichier:
    texte = fichier.read()

def t():
    Voyelles = ['a', 'e', 'i', 'o', 'u','y']
    var = "tttttt"
    while not(var[1] in Voyelles and var[3] in Voyelles) or var[2] in Voyelles:
        var = ""
        for i in range(6):
            var = var + chr(random.randint(97, 122))
    return var

def lettre_apres(letter):
    #Cette fonction consiste à donner une lettre aléatoire qui a une probabilité d'arriver après la lettre entrée
    #Sauf les espaces, les caractères spéciaux et le S après le T
    j = 0
    i = random.randint(0, 3733441)
    while j == 0 :
        i = i + 1
        if texte[i]==letter:
            if not(texte[i+1]=='\n'):
                j = 1
                return texte[i+1]