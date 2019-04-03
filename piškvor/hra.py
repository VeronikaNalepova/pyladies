from piskvorky import tah_hrace, vyhodnot
from ai import tah_pocitace
from util import tah, delka_pole


def piskvorky1d():
    DELKA_POLE = delka_pole()

    pole = DELKA_POLE * "-"
    while True:
        print(pole)
        pole = tah_hrace(pole)
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
DELKA_POLE = delka_pole()

piskvorky1d()
