class DeretAngka:
    def __init__(self, nim_angka_terakhir):
        self.nim_angka_terakhir = nim_angka_terakhir

    def tampilkan_deret(self):
        for i in range(1, 51):
            if i % 100 != self.nim_angka_terakhir:
                print(i, end=" ")

def main():
    nim_angka_terakhir = int(input("Masukkan 2 digit terakhir dari NIM Anda: "))
    deret = DeretAngka(nim_angka_terakhir)
    print("Deret angka kecuali 2 digit terakhir NIM Anda:")
    deret.tampilkan_deret()

if __name__ == "__main__":
    main()
