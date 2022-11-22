import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_ostoskorin_hinta_yhden_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)

        self.assertEqual(self.kori.hinta(), 5)     

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_kaksi_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)

    def test_ostoskori_sisaltaa_yhden_tuotteen_sen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskori_sisaltaa_yhden_tuotteen_sen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_ostoskorissa_kaksi_tuotetta_kahden_tuotteen_lisaamisen_jalkeen(self):
        maito = Tuote("Maito", 3)
        voi = Tuote("Voi", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(voi)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_ostoskorissa_yksi_ostos_kun_lisatty_kaksi_kertaa_sama_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_ostoskori_sisaltaa_kaksi_kappaletta_samaa_tuotetta_kun_se_lisatty_kahdesti(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_ostoskorissa_tuotetta_yksi_kappale_jos_kahdesta_toinen_poistetaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_ostoskori_on_tyhja_jos_ainoa_tuote_poistetaaan(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 0)