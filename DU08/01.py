def nta_mocnina():
    """Zjistí od uživatele proměnou kterou má zadat"""
    while True:
        odpoved= input("Zadejí číslo a já ti řeknu jaký je jeho součet na druhou a součet čísla ")
        try:
            n = int(odpoved)
        except ValueError:
            print("Špatně zadaná n-tá mocnina nevím co chceš počítat!!!")
        else:
            break
    return n

def suma_mocnin(n):
    """Vypočte sumu klíčů a sumu hodnot"""
    cislona2={(x,x**2) for x in range(n+1)}
    mocniny=dict(cislona2)

    print(sum(mocniny.values())) #suma hodnot
    print(sum(mocniny.keys())) #suma klíčů

n = nta_mocnina()
suma_mocnin(n)
