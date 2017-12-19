#!/usr/bin/python3
def clear():
    import os
    os.system("cls" if os == "nt" else "clear")

    print("Mõtte kuvamiseks vajuta 'Enter'.")
    print("Ekraani puhastamiseks vajuta 'c'.")
    print("Mõtte lisamiseks vajuta 'a'.")
    print("Väljumiseks vajuta 'e'.")
#Defineerin programmist väljumise:
def exit():
    import sys
    import os
    os.system("cls" if os == "nt" else "clear")
    sys.exit()
#Defineerin suvalise mõtte kuvamise:
def kuva():
    import random
    with open("Aforismid","r") as fail:
        sisu = fail.readlines()
        print(random.choice(sisu))
#Defineerin mõtte lisamise:
def lisa():
    with open("Aforismid", "a") as fail:
        mote = input("Lisa mõte:\n> ")
        print("Kas soovid mõtte salvestada? y/n")
        kinnitus = input("> ")
        if kinnitus == "y" or kinnitus == "Y":
            print(mote)
            fail.write(str(mote+"\n"))
            print("[+]")
            main()
        else:
            clear()
            main()
#Defineerin programmi tuuma:
def main():
    valik = input("> ")

    if valik == "e" or valik == "E":
        exit()
    elif valik == "a" or valik == "A":
        lisa()
        main()
    elif valik == "":
        kuva()
        main()
    elif valik == "c" or valik == "C":
        clear()
        main()

clear()
main()
