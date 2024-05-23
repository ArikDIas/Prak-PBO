class Overloading:
    @staticmethod
    def Tambah(x, y=None):
        if y is None:
            return Overloading.TambahInt(x)
        else:
            return Overloading.TambahFloat(x, y)
    
    @staticmethod
    def TambahInt(x):
        return x
    
    @staticmethod
    def TambahFloat(x, y):
        return x + y

bil1 = Overloading.Tambah(9)
bil2 = Overloading.Tambah(3.5, 5.7)
print("int", bil1)
print("float", bil2)
