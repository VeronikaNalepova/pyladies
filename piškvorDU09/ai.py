from util import tah, DELKA_POLE
from random import randrange

def tah_pocitace(pole, symbol = "o"):

    if len(pole) > DELKA_POLE or len(pole) < DELKA_POLE:
        raise ValueError("Pole musí být rovno definované délce pole")
    elif len(pole) == 0:
        raise ValueError("Pole nemůže být nulové")
    elif pole == '          ':
        raise ValueError("Pole musí být vyplněno")
    elif pole == 'oxoxoxoxox':
        raise ValueError("Pole nemůže být plnné")


    while True:
        cislo_policka=randrange(DELKA_POLE)
        if pole[cislo_policka] =="-":
            return tah(pole, cislo_policka, "o")



    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pass
