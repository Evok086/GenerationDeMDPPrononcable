import random

def t():
    Voyelles = ['a', 'e', 'i', 'o', 'u']
    var = "ttt"
    while var[1] != Voyelles[0] and var[1] != Voyelles[1] and var[1] != Voyelles[2] and var[1] != Voyelles[3] and var[1] != Voyelles[4]:
        var = ""
        for i in range(3):
            var = var + chr(random.randint(97, 122))
    return var
