class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
        self.grade = self.hitung_grade()

    def hitung_grade(self):
        if 80 <= self.nilai <= 100:
            return 'A'
        elif 77 <= self.nilai <= 79:
            return 'A-'
        elif 74 <= self.nilai <= 76:
            return 'B+'
        elif 68 <= self.nilai <= 73:
            return 'B'
        elif 65 <= self.nilai <= 67:
            return 'B-'
        elif 62 <= self.nilai <= 64:
            return 'C+'
        elif 56 <= self.nilai <= 61:
            return 'C'
        elif 45 <= self.nilai <= 55:
            return 'D'
        else:
            return 'E'

# Meminta input dari pengguna
try:
    print("--- DATA PRAKTIKAN PBO 2024 ---")
    nama_mahasiswa = input("Nama: ")
    nim_mahasiswa = input("Nim: ")
    nilai_mahasiswa = float(input("Masukkan nilai: "))
    if 0 <= nilai_mahasiswa <= 100:
        # Membuat objek Mahasiswa
        mahasiswa = Mahasiswa(nama=nama_mahasiswa, nilai=nilai_mahasiswa)
        # Menampilkan hasil
        print(f"Grade: {mahasiswa.grade}")
    else:
        print("Nilai tidak valid. Harap masukkan nilai antara 0 dan 100.")
except ValueError:
    print("Input tidak valid. Harap masukkan nilai numerik.")
