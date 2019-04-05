DELKA_POLE = 10
if DELKA_POLE < 5:
    raise ValueError('Číslo hracího pole musí být větší nebo rovno 5')


def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    pass
