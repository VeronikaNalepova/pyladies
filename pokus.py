import random
seznam=["coko", "koko", "parek"]
SLOVO = random.choice(seznam)

def uhadni(pole, pismeno, SLOVO):
    for index in range(len(SLOVO)):
        if pismeno == SLOVO[index]:
            pole = pole[:index]+pismeno+pole[index+1:]
            return pole
"""Vrátí herní pole s písmenem"""

def sibenice():
    pokus=0
    pole=len(SLOVO)*"-"
    print(pole)
    while True:
        pismeno=input("Zahrajem si šibenici. Uhádneš slovo? Zadej písmeno ")
        if pismeno in SLOVO:
            pole = uhadni(pole, pismeno, SLOVO)
            print(pole)
            if "-" not in pole:
                print("Gratuluji vyhrál jsi")
                break
        else:
            pokus+=+1
            print("Neuhádl si máš", pokus, "špatný pokus asi tě oběsíme")
            with open ("panak.txt", encoding='utf-8') as soubor:
                obsah = soubor.read(3*pokus)
                print(obsah)
                if pokus==14:
                    print("Prohrál jsi")
                    break

    while True:
        odpoved=input("Chceš hrát znovu? odpověz ano/ne ")
        if odpoved=="ano":
            return sibenice()
        elif odpoved=="ne":
            print("Škoda")
            break
        else:
            print("Nerozumím ano nebo ne? ")
sibenice()
