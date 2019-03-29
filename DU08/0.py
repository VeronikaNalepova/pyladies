def cislo_na_druhou(n):
    """Funkce vytvoří slovník mocninu čísla na 2"""

    cislona2={(x,x**2) for x in range(n+1)}
    mocniny=dict(cislona2)
    print(mocniny)

cislo_na_druhou(10)
