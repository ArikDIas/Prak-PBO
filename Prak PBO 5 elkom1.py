class Film:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, judul):
        self.daftar_film.append(judul)

    def tampilkan_film(self):
        print("5 film favorit kamu nih:")
        for film in self.daftar_film:
            print(film)


def main():
    film_favorit = Film()

    print("-----Elkom 1-----")
    for i in range(5):
        film_favorit.tambah_film(input(f"Film favorite ke-{i+1}: "))

    print("\n===Daftar Film Favorite===")
    film_favorit.tampilkan_film()


if __name__ == "__main__":
    main()