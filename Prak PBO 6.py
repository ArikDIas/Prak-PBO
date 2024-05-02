import math

class BangunRuang:
    def __init__(self):
        pass
    
    def hitung_luas(self):
        pass
    
    def hitung_volume(self):
        pass

class Kubus(BangunRuang):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi
    
    def hitung_luas(self):
        return 6 * self.sisi ** 2
    
    def hitung_volume(self):
        return self.sisi ** 3

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
    
    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

class Bola(BangunRuang):
    def __init__(self, jari_jari):
        super().__init__()
        self.jari_jari = jari_jari
    
    def hitung_luas(self):
        return 4 * math.pi * self.jari_jari ** 2
    
    def hitung_volume(self):
        return (4/3) * math.pi * self.jari_jari ** 3

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
    
    def hitung_volume(self):
        return math.pi * self.jari_jari ** 2 * self.tinggi

class LimasSegitiga(BangunRuang):
    def __init__(self, alas, tinggi_alas, tinggi):
        super().__init__()
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        luas_permukaan_segitiga = self.alas * self.tinggi_alas / 2
        luas_permukaan_limas = self.alas * self.tinggi_alas + 3 * luas_permukaan_segitiga
        return luas_permukaan_limas
    
    def hitung_volume(self):
        return (self.alas * self.tinggi_alas * self.tinggi) / 3

# Main program
def main():
    kubus = Kubus(5)
    balok = Balok(3, 4, 5)
    bola = Bola(4)
    tabung = Tabung(3, 6)
    limas = LimasSegitiga(6, 8, 10)
    
    print("Luas Kubus:", kubus.hitung_luas(), "\nVolume Kubus:", kubus.hitung_volume(), "\n")
    print("Luas Balok:", balok.hitung_luas(), "\nVolume Balok:", balok.hitung_volume(), "\n")
    print("Luas Bola:", bola.hitung_luas(), "\nVolume Bola:", bola.hitung_volume(), "\n")
    print("Luas Tabung:", tabung.hitung_luas(), "\nVolume Tabung:", tabung.hitung_volume(), "\n")
    print("Luas Limas:", limas.hitung_luas(), "\nVolume Limas:", limas.hitung_volume(), "\n")

if __name__ == "__main__":
    main()
