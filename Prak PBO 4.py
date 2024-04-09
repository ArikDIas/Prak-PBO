class Student:
    data_pribadi = "---Data Pribadi---"

    def __init__(self, nama):
        self.nama = nama
        self.nim = None
        self.nilai = None

    def set_nim(self, nim):
        self.nim = nim

    def set_nilai(self, nilai):
        self.nilai = nilai

    def print_data(self):
        print(self.data_pribadi)
        print("Nama:", self.nama)
        print("NIM:", self.nim)
        print("Nilai:", self.nilai)

    @staticmethod
    def print_data_teman(nomor_teman, teman):
        print("Teman", nomor_teman, ":", teman)


# Main program
if __name__ == "__main__":
    students = []

    while True:
        nama = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk mengakhiri): ")
        if nama.lower() == 'selesai':
            break

        student = Student(nama)
        nim = input("Masukkan NIM mahasiswa: ")
        student.set_nim(nim)
        nilai = float(input("Masukkan nilai mahasiswa: "))
        student.set_nilai(nilai)

        students.append(student)

    print("\nData Mahasiswa:")
    for i, student in enumerate(students, start=1):
        print(f"\nData Mahasiswa ke-{i}:")
        student.print_data()


