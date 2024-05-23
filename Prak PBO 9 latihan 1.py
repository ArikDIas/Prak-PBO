import math

class BangunRuang:
    def hitung_volume(self):
        return 0

class Kubus(BangunRuang):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_volume(self):
        volume = self.sisi ** 3
        return f"volume kubus dengan sisi {self.sisi} adalah {volume}cm^3"

class Balok(BangunRuang):
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    
    def hitung_volume(self):
        volume = self.panjang * self.lebar * self.tinggi
        return f"volume balok dengan panjang {self.panjang}, lebar {self.lebar}, dan tinggi {self.tinggi} adalah: {volume}cm^3"

class Tabung(BangunRuang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
    
    def hitung_volume(self):
        volume = math.pi * self.jari_jari ** 2 * self.tinggi
        return f"volume tabung dengan jari-jari {self.jari_jari} dan tinggi {self.tinggi} adalah: {volume:.2f}cm^3"

def main():
    kubus = Kubus(9)
    print(kubus.hitung_volume())

    balok = Balok(4, 9, 5)
    print(balok.hitung_volume())

    tabung = Tabung(3, 7)
    print(tabung.hitung_volume())

if __name__ == "__main__":
    main()
