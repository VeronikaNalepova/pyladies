class Ctverec:
    def __init__(self, strana):
        self.strana = strana

    def obvod(self):
        obvod = 4 * self.strana
        return obvod

    def obsah(self):
        obsah = self.strana * self.strana
        return obsah

    def rozdil_obsahu(self):
        rozdil = ctverec1.obsah() - ctverec2.obsah()
        return rozdil

ctverec1 = Ctverec(5)
ctverec1.obvod()
ctverec1.obsah()
ctverec2 = Ctverec(4)
ctverec2.obsah()
ctverec2.rozdil_obsahu()
