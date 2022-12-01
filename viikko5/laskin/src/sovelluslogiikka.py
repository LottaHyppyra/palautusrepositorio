class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = tulos

    def edellinen_tulos_talteen(self): 
        self.edellinen = self.tulos

    def miinus(self, arvo):
        self.edellinen_tulos_talteen()
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen_tulos_talteen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.edellinen