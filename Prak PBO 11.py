class FullNameGenerator:
    def add_nim(func):
        def wrapper(self, nama_depan, nama_belakang, panggilan, nim):
            full_name = func(self, nama_depan, nama_belakang, panggilan)
            return full_name + " " + nim
        return wrapper

    @add_nim
    def generate_full_name(self, nama_depan, nama_belakang, panggilan):
        return f"{panggilan} {nama_depan} {nama_belakang}"

nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
panggilan = input("Masukkan panggilan (Mr./Ms.): ")
nim = input("Masukkan NIM: ")

generator = FullNameGenerator()
print("Full Name:", generator.generate_full_name(nama_depan, nama_belakang, panggilan, nim))
