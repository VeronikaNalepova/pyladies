def pocet_znaku(slovo):
    """ Zobrazí slovník zadaného argumentu rozdělený na počet slov"""

    klic_slovo=list(slovo)      #převede slovo na seznam = vytovří key pro slovník

    hodnoty=[]
    for znak in klic_slovo:
        hodnoty.append(klic_slovo.count(znak))          #vytvoří hodnoty pro slovník do seznamu


    ntice_slovo=[]
    for klic_slovo, hodnoty in zip(klic_slovo, hodnoty):
        ntice_slovo.append('{} = {}'.format(klic_slovo, hodnoty))       #spojí hodnoty do n-tic

    ntice_slovo_podlis = [v.split('=',1) for v in ntice_slovo if '=' in v]    #rozeká seznam na podsenamy
                                                                                #aby šel vytvořit slovník

    slovník_slovo = dict(ntice_slovo_podlis)
    print(slovník_slovo)

slovo=input("Napiš slovo a ja ho rozsekám do slovníku ")
pocet_znaku(slovo)
