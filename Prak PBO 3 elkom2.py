class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def tampilkan_persegi_panjang(self):
        return f"Persegi panjang dengan panjang {self.panjang}cm dan lebar {self.lebar}cm"

# Contoh penggunaan
persegi_panjang1 = PersegiPanjang(5, 8)
print(persegi_panjang1.tampilkan_persegi_panjang() + f" memiliki luas sebesar {persegi_panjang1.hitung_luas()}cm^2")
