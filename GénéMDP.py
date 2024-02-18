import random
with open("liste_de_mots_francais.txt", encoding='utf8') as fichier:
    texte = fichier.read()

def lettre_apres(letter):
    #Cette fonction consiste à donner une lettre aléatoire qui a une probabilité d'arriver après la lettre entrée sauf les espaces et les caractères spéciaux
    j = 0
    i = random.randint(0, 1866720)
    condition = False
    while j == 0 :
        i = i + 1
        if letter == 's' or letter == 't' or letter == 'r':
            condition = texte[i+1]=='s' or texte[i+1]=='t' or texte[i+1]=='r'
        if letter == 'i':
            condition = texte[i+1]=='e'
        if letter == 'e':
            condition = texte[i+1]=='a'
        if texte[i]==letter and not(texte[i+1]=='\n' or texte[i+1]==' ' or texte[i+1]=='-' or texte[i+1]=='é' or texte[i+1]=='à' or texte[i+1]=='ç' or texte[i+1]=='ù' or texte[i+1]=='î' or texte[i+1]=='ê' or texte[i+1]=='è' or texte[i+1]=='â' or condition) :
            j = 1
            return texte[i+1]
            
def mdp(long):
    mdp = chr(random.randint(97, 122))
    for _ in range(long-1):
        mdp = mdp + lettre_apres(mdp[len(mdp)-1])
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
    
