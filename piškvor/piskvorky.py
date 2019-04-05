from util import tah, DELKA_POLE
from ai import tah_pocitace

def vyhodnot(pole):
    if "xxx" in pole:
        return("x")
    elif "ooo" in pole:
        return("o")
    elif "-" not in pole:
        return("!")
    else:
        return("-")
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
    pass


def tah_hrace(pole, symbol = "x"):
    while True:
        cislo_policka = int(input("Na které pole chceš táhnout? "))
        if cislo_policka >= 0 and cislo_policka < DELKA_POLE and pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, "x")
        else:
            print("špatně zadané pole, zkus to znovu")
        """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    pass

def piskvorky1d():
    DELKA_POLE = 10
    if DELKA_POLE < 5:
        raise ValueError('Číslo hracího pole musí být větší nebo rovno 5')


    pole = DELKA_POLE * "-"
    while True:
        print(pole)
        pole = tah_hrace(pole, "x")
        print(pole)
        if vyhodnot(pole) !="-":
            break
        pole = tah_pocitace(pole, "o")
        if vyhodnot(pole) !="-":
            break

        pass
    """
    Hraje 1D piškvorky.
    """
    pass

    if vyhodnot(pole) == "x":
        print("Vyhrál člověk")
    elif vyhodnot(pole) == "o":
        print("Vyhrál počítač")
    elif vyhodnot(pole) == "!":
        print("Remíza")
