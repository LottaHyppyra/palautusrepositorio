from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for ostos in self._ostokset.keys():
            lkm = self._ostokset[ostos]
            maara += lkm
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for ostos in self._ostokset.keys():
            tuotteen_hinta = ostos.hinta()
            lkm = self._ostokset[ostos]
            hinta += tuotteen_hinta * lkm
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        lisattava_nimi = lisattava.nimi()
        for ostos in self._ostokset.keys():
            if ostos.tuotteen_nimi() == lisattava_nimi:
                self._ostokset[ostos] += 1
                return
        self._ostokset[Ostos(lisattava)] = 1

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._ostokset.keys())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
