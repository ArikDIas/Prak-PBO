class Penjumlahan:
    def pertambahan(self):
        angka_1 = float(input("Masukkan angka 1 : "))
        angka_2 = float(input("Masukkan angka 2 : "))

        hasil = angka_1 + angka_2    #Penjumlahan

        print(f"hasilnya = {hasil}")


calculator = Penjumlahan()
calculator.pertambahan()