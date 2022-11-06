import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54), 
            Player("Kurri",   "EDM", 37, 53), 
            Player("Yzerman", "DET", 42, 56), 
            Player("Gretzky", "EDM", 35, 89) 
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

        self.pelaajat = self.statistics.players()

    def test_etsi_pelaaja_toimii(self):
        oikea_pelaaja = self.pelaajat[4]
        
        self.assertAlmostEqual(self.statistics.search("Gretzky"), oikea_pelaaja)

    def test_palauttaa_none_kun_pelaaja_ei_listalla(self):
        self.assertAlmostEqual(self.statistics.search("-"), None)


    def test_palauttaa_oikean_tiimin(self):
        EDM_pelaajat = [self.pelaajat[0], self.pelaajat[2], self.pelaajat[4]]

        self.assertAlmostEqual(self.statistics.team("EDM"), EDM_pelaajat)

    def test_pelaajat_top_jarjestyksessa(self):
        top_pelaajat = [self.pelaajat[4], self.pelaajat[1], self.pelaajat[3], self.pelaajat[2]]

        self.assertAlmostEqual(self.statistics.top(3), top_pelaajat)

    def test_pelaajat_top_points_jarjestyksessa(self):
        top_pelaajat = [self.pelaajat[4], self.pelaajat[1], self.pelaajat[3], self.pelaajat[2]]
    
        self.assertAlmostEqual(self.statistics.top(3, 1), top_pelaajat)

    def test_pelaajat_top_goals_jarjestyksessa(self):
        top_pelaajat = [self.pelaajat[1], self.pelaajat[3], self.pelaajat[2], self.pelaajat[4]]
        
        self.assertAlmostEqual(self.statistics.top(3, 2), top_pelaajat)

    def test_pelaajat_top_assists_jarjestyksessa(self):
        top_pelaajat = [self.pelaajat[4], self.pelaajat[3], self.pelaajat[1], self.pelaajat[2]]
        
        self.assertAlmostEqual(self.statistics.top(3, 3), top_pelaajat)  