class Segitiga:
    def __init__(self, alas=0, tinggi=0, sisi1=0, sisi2=0, sisi3=0):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi1 = sisi1
        self.sisi2 = sisi2
        self.sisi3 = sisi3

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return self.sisi1 + self.sisi2 + self.sisi3

def input_alas_dan_tinggi():
    return float(input("Masukkan panjang alas segitiga: ")), float(input("Masukkan tinggi segitiga: "))

def input_sisi():
    return float(input("Masukkan panjang sisi pertama segitiga: ")), float(input("Masukkan panjang sisi kedua segitiga: ")), float(input("Masukkan panjang sisi ketiga segitiga: "))

def main():
    print("PROGRAM MENGHITUNG KELILING DAN LUAS SEGITIGA:")
    print("1. Luas segitiga")
    print("2. Keliling segitiga")
    pilihan = input("Masukkan nomor pilihan Anda: ")

    if pilihan == '1':
        alas, tinggi = input_alas_dan_tinggi()
        print("Luas segitiga adalah:", Segitiga(alas=alas, tinggi=tinggi).hitung_luas())
    elif pilihan == '2':
        sisi1, sisi2, sisi3 = input_sisi()
        print("Keliling segitiga adalah:", Segitiga(sisi1=sisi1, sisi2=sisi2, sisi3=sisi3).hitung_keliling())
    else:
        print("Pilihan tidak valid. Silakan masukkan nomor 1 atau 2.")

if __name__ == "__main__":
    main()
