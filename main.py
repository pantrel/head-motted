#!/usr/bin/python3
def clear():
    import os
    os.system("cls" if os == "nt" else "clear")
def tervitus():
    print("---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---")
    print("Oled kasutamas heade mõtete kuvamise programmi!")
    print("Suvalise mõtte kuvamiseks vajuta 'Enter'.")
    print("Ekraani puhastamiseks sisesta 'c'.")
    print("Mõtte lisamiseks sisesta 'a'.")
    print("Väljumiseks sisesta 'e'.")
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
        sisu = fail.read().splitlines()
        print(random.choice(sisu)+"\n")

#Defineerin mõtte lisamise:
def lisa():
    with open("Aforismid", "a") as fail:
        mote = input("---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---\nSisesta mõte:\n> ")
        print("Kas soovid mõtte salvestada? y/n")
        kinnitus = input("> ")
        print(mote)
        if kinnitus == "y" or kinnitus == "Y":
            fail.write(str(mote+"\n"))
            clear()
            tervitus()
            main()
        else:
            clear()
            tervitus()
            main()
#Defineerin programmi tuuma:
def main():
    valik = input("---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---\n")

    if valik == "e" or valik == "E":
        exit()
    elif valik == "a" or valik == "A":
        clear()
        tervitus()
        lisa()
        main()
    elif valik == "":
        kuva()
        main()
    elif valik == "c" or valik == "C":
        clear()
        tervitus()
        main()

clear()
tervitus()
main()
