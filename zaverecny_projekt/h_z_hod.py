def velikost_hraciho_pole():
    """Zjistí od uživatele rozumnou velikost herního pole"""
    while True:
        odpoved = input('Zadej velikost pole pro hada: ')
        try:
            velikost = int(odpoved)
        except ValueError:
            print('Velikost musí být celé číslo')
        else:
            if velikost > 5:
                break
            else:
                print('Pole musí být rozumně veliké!')

    return velikost

def vykresli_mapu(velikost, had, ovoce):
    """Vykreslí herní mapu s ovocem a hadem na správných místech"""
    for x in range(velikost):
        for y in range(velikost):
            if (x, y) in had:
                print('X', end=' ')
            elif (x, y) in ovoce:
                print('?', end=' ')
            else:
                print('.', end=' ')
        print()

def posun(velikost, had, ovoce):
    """Posune hada v určitém směru a zajistí jeho prodloužení při snězení jídla"""
    while True:
        smer = input('Zadej smer posunu [s, j, v, z]: ')
        smer = smer.lower().strip()
        if smer not in ('s', 'j', 'v', 'z'):
            print('Nekorektni smer!')
        else:
            break

    hlava = had[-1]
    x, y = hlava
    if smer == 's':
        nova_hlava = x-1, y
    elif smer == 'j':
        nova_hlava = x+1, y
    elif smer == 'v':
        nova_hlava = x, y+1
    elif smer == 'z':
        nova_hlava = x, y-1

    if nova_hlava in had:
        raise ValueError('GAME OVER! Narazil si sam do sebe')

    x, y = nova_hlava

    if x < 0 or x > velikost-1 or y < 0 or y > velikost-1:
        raise ValueError('GAME OVER! Vyjel si mimo herni pole')

    if nova_hlava in ovoce:
        ovoce.remove(nova_hlava)
    else:
        del had[0]

    had.append(nova_hlava)
    return True

from random import randrange

def pridej_ovoce(velikost, had, ovoce):
    """Přidá další ovoce na herní plochu mimo souřadnice hada"""
    ovoce.append((randrange(0, velikost), randrange(0, velikost)))
    while ovoce[-1] in had:
        del ovoce[-1]
        ovoce.append((randrange(0, velikost), randrange(0, velikost)))

def hra():
    """Hlavní části hry spojeny ve finální celek"""
    velikost = velikost_hraciho_pole()

    had = [(0, 0), (0, 1), (0, 2)]
    ovoce = []
    pridej_ovoce(velikost, had, ovoce)

    vykresli_mapu(velikost, had, ovoce)

    while posun(velikost, had, ovoce):
        vykresli_mapu(velikost, had, ovoce)
        if not ovoce:
            pridej_ovoce(velikost, had, ovoce)

hra()
