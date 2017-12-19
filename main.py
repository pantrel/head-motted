#!/usr/bin/python3
def clear():
    import os
    os.system("cls" if os == "nt" else "clear")


def kuva():
    pass

def lisa():
    pass

while True:

    print("Mõtte kuvamiseks vajuta 'Enter'.")
    print("Mõtte lisamiseks vajuta 'a'.")
    print("Väljumiseks vajuta 'e'.")

    valik = input("> ")

    if valik == "e" or "E":
        import sys
        clear()
        sys.exit()
    elif valik == "a" or "A":
        pass
    else:
        pass
