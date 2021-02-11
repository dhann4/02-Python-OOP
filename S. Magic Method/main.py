class Mangga:

    # Magic Method
    # yang pertama, Standar Magic Method yaitu __init__()
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # yang kedua, __repr__() di pakai saat debuging
    # def __repr__(self):
    #     return "Debug : Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    # yang ketiga, __str__() di pakai saat programnya sudah selesai
    def __str__(self):
        return "Mangga: {} dengan jumlah: {}".format(self.nama, self.jumlah)

    # yang keempat,__add__() berguna untuk aritmatika / menjumlahkan dua buah objek
    def __add__(self, objek):
        return self.jumlah + objek.jumlah

    # yang kelima, __dict__()
    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"

belanja1 = Mangga('Arumanis', 10)
belanja2 = Mangga('Nanas', 5)

# print(repr(belanja1))
print(belanja1)
print(belanja2)

print('total jumlah:', belanja1 + belanja2)

print(belanja1.__dict__)
