class Praktikan:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def tampilkan_identitas(self):
        return f"Nama saya adalah {self.nama} NIM saya {self.nim}.\nSaya dari fakultas {self.fakultas}.\nHobi saya adalah: {self.hobi}"

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_fakultas(self):
        return self.fakultas

    def get_hobi(self):
        return self.hobi

# Contoh penggunaan
praktikan1 = Praktikan("Arik Dias Putra", "064002300021", "Teknik Informatika", "Tidur")
print(praktikan1.tampilkan_identitas())
