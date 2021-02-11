class Hero:

    # Class Variable
    jumlah = 0
    __privateJumlah = 0


    def __init__(self, name, health):
        self.name = name
        self.health = health

        # Variable Instance Private
        self.__private = 'Private'

        # Variable Instance Protected
        self._protected = "Protected"

lina = Hero('Lina', 100)

# print(lina.__dict__)
# print(lina.__private)
# lina.__private = 'testing'

# print(lina.__dict__)
# print(lina.__private)  # Akan Error, karena Hero tidak mempunyai attribute __private.
# Si __private ini tidak bisa di akses dan bersifat Private


# print(lina.__dict__)
# print(lina._protected)
# lina._protected = 'testing'
#
# print(lina.__dict__)
# print(lina._protected)

print(lina.__dict__)
print(Hero.__dict__)