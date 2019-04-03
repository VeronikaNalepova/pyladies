def delka_pole():
    '''Vrátí délku hracího pole a ověří zda je délka správná'''

    DELKA_POLE = 25
    if DELKA_POLE < 5:
        raise ValueError('Číslo hracího pole musí být větší nebo rovno 5')

    return DELKA_POLE


def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka+1:]
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    pass
