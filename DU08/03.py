from collections import OrderedDict
def vypis_slovnik(slovnik):
    """Vypíše slovník do řádků pod sebe"""

    for keys, values in d.items():
        print(keys, values)

d= OrderedDict()
d={'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
vypis_slovnik(d)
