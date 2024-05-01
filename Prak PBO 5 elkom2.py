class Film:
    def __init__(self, judul, tahun_rilis, director):
        self.judul = judul
        self.tahun_rilis = tahun_rilis
        self.director = director

class DaftarFilm:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, film):
        self.daftar_film.append(film)

    def tampilkan_daftar(self):
        print("Daftar Film Favorit:")
        for film in self.daftar_film:
            print(f"Judul: {film.judul}")
            print(f"Tahun Rilis: {film.tahun_rilis}")
            print(f"Director: {film.director}")
            print()

def main():
    daftar_film = DaftarFilm()

    print("-----Elkom 1-----")
    for i in range(5):
        judul = input(f"Film favorit ke-{i+1}: ")
        tahun_rilis = input(f"Tahun rilis {judul}: ")
        director = input(f"Nama director {judul}: ")
        film = Film(judul, tahun_rilis, director)
        daftar_film.tambah_film(film)

    print("\n===Daftar Film Favorite===")
    daftar_film.tampilkan_daftar()

if __name__ == "__main__":
    main()
