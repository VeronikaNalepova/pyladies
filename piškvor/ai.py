from util import tah, delka_pole
from random import randrange

def tah_pocitace(pole, o):
    while True:
        cislo_policka=randrange(DELKA_POLE)
        if pole[cislo_policka] =="-":
            return tah(pole, cislo_policka, "o")

    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pass
