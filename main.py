#!/usr/bin/python3
import os, sys, random, textwrap  ## OSiga suhtlemiseks ja suvaliste arvude
                        # genereerimiseks vajalike teekide importimine.

punktiir      = "---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---"
kogutud_mõtted  = []    ## Muutujad kasutajaliideses paljukasutatava sõne
ajutised_mõtted = []    #  punktiir jaoks ning mõtete haldamiseks.

## Funktsioonid.

def puhasta_ekraan(): # Mugvadusfunktsioon terminali tekstist puhastamiseks.
    os.system("cls" if os == "nt" else "clear") # Kontrollib, kas OS on Windows
                                                # või UNIX tüüpi ja valib
                                                # sobiva käskluse.
def täida_järjend(fail, *järjendid):
    with open(fail, "r") as fail:
        for rida in fail:
            [järjend.append(rida) for järjend in järjendid]

def taaslae_järjend():
    if len(ajutised_mõtted) != 0:
        ajutised_mõtted.clear()
        [ajutised_mõtted.append(mõte) for mõte in kogutud_mõtted]
    else:
        [ajutised_mõtted.append(mõte) for mõte in kogutud_mõtted]

def kuva_fail(fail):
    with open(fail, "r") as fail:
        [print(rida.strip()) for rida in fail]

def tervitus():
    print("{}\n".format(punktiir))
    kuva_fail(".tervitus")
    print("\n{}\n".format(punktiir))

def exit(): ## Programmist väljumine.
    puhasta_ekraan()
    sys.exit()

def kuva(): # Suvaliselt valitud mõtte kuvamine.
    puhasta_ekraan()
    tervitus()
    with open("Aforismid","r") as fail:
        try:
            [print(rida) for rida in textwrap.wrap(ajutised_mõtted.pop(random.randint(0,len(ajutised_mõtted)) -1), width=69)]
            main()
        except IndexError:
            print("Mõtted on otsas. Kogu mõtteid või lisa neid juurde! :)")
            main()

def lisa(): ## Mõtte lisamine.
    puhasta_ekraan()
    tervitus()
    mõte  = input(punktiir+"\n/Sisesta mõte/>> ")
    autor = input(punktiir+"\n/Mõtte autor/>> ")
    print("Kas soovid mõtte salvestada? (j/e)")
    kinnitus= input(">> ")
    if kinnitus == "j" or kinnitus == "J":
        kogutud_mõtted.append('"{}" ({})\n'.format(mõte.capitalize(), autor.title()))
        with open("Aforismid", "a") as fail:
            fail.write('"{}" ({})\n'.format(mõte.capitalize(), autor.title()))
        puhasta_ekraan()
        print("[+] Lisatud!")
        tervitus()
        main()
    else:
        puhasta_ekraan()
        tervitus()
        main()

def main(): ## Programmi tuum.
    try:    #  Kontrollib, kas kogutud mõtteid ei ole, sellisel juhul täidab
        if len(kogutud_mõtted) == 0:               # kogutud mõtete järjendi.
            täida_järjend("Aforismid", kogutud_mõtted)

        valik = input("\n{}\n".format(punktiir))

        if valik == "v" or valik == "V":
            exit()
        elif valik == "l" or valik == "L":
            lisa()
        elif valik == "p" or valik == "P":
            puhasta_ekraan()
            tervitus()
            main()
        elif valik == "k" or valik == "K":
            taaslae_järjend()
            puhasta_ekraan()
            tervitus()
            main()
        elif valik == "":
            kuva()
        else:
            tervitus()
            main()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    puhasta_ekraan()
    tervitus()
    täida_järjend("Aforismid", kogutud_mõtted, ajutised_mõtted)
    main()
