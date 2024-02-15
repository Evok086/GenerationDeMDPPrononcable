import random

def t():
    Voyelles = ['a', 'e', 'i', 'o', 'u','y']
    var = "tttttt"
    while not(var[1] in Voyelles and var[3] in Voyelles) or var[2] in Voyelles:
        var = ""
        for i in range(6):
            var = var + chr(random.randint(97, 122))
    return var
