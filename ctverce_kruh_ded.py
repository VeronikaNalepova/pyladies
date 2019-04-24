from math import pi

class Geo_utvary():

    def rozdil_obsahu(self, druhy_utvar):
        print(self.obsah() - druhy_utvar.obsah())

class Ctverec(Geo_utvary):
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        return 4 * self.strana

    def obsah(self):
        return self.strana ** 2

class Kruh(Geo_utvary):
    def __init__(self, polomer):
        self.polomer = polomer

    def obsah(self):
        return pi * self.polomer **2

    def obvod(self):
        return 2 * pi * self.polomer

class Obdelnik(Geo_utvary):
    def __init__(self, strana_a, strana_b):
        self.strana_a = strana_a
        self.strana_b = strana_b

    def obvod(self):
        return 2*(self.strana_a + self.strana_b)

    def obsah(self):
        return self.strana_a * self.strana_b

ctverec1= Ctverec(5)
obdelnik1=Obdelnik(4, 5)
ctverec1.rozdil_obsahu(obdelnik1)
kruh1 = Kruh(4)
obdelnik1.rozdil_obsahu(kruh1)
