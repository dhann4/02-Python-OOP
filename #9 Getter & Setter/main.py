# memakai Getter dan Setter yang di pakai di python

class Hero:

    def __init__(self, name, health, armor):
        # self.__name = name
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\t health: {}".format(self.name, self.__health)

    # tidak otomatis terupdate dengan nama baru karena hanya berubah saat di awal saja atau saat memakai __init__()
    # jika di dalam __init__() ada self.info = "name {} : \n\t health: {}".format(self.name, self.__health)
    # tidak akan berubah dan namanya tetap menjadi sniper

    # Property = mengubah method menjadi seperti variable
    #@property
    #def info(self):
        # return "name {} : \n\t health: {}".format(self.__name, self.__health)
    # atau bisa juga dengan
        # return self.__info (sama saja seperti geter)

    # tapi jika seperti ini
    @property
    def info(self):
        return "name {} : \n\t health: {}".format(self.name, self.__health)
    # saat kita ubah nama si sniper menjadi dadang, maka si sniper akan berubah menjadi dadang

    # hasilnya akan none karena tidak terdapat objek di dalam nya
    @property
    def armor(self):
        pass

    # hasilnya akan mengikuti hasil dari armor karena terdapat objek __armor di dalam nya karena menggunakan getter
    # dan tidak bisa di ubah karena hasil nya akan mengikuti hasil dari default nya armor di dalam __init__()
    @armor.getter
    def armor(self):
        return self.__armor

    # jika ingin mengubah variable armor nya cukup gunakan setter caranya adalah
    @armor.setter
    def armor(self, input):
        self.__armor = input

    # deleter
    @armor.deleter
    def armor(self):
        print('armor di deleter')
        self.__armor = None

sniper = Hero("Sniper", 100, 10)

print('merubah info:')
print(sniper.info)

sniper.name = 'dadang'
print(sniper.info)
# tapi jika di dalam property nya seperti ini
# @property
# def info(self):
#     return "name {} : \n\t health: {}".format(self.name, self.__health)
# maka akan langsung otomatis nama nya berganti jadi sniper menjadi dadang

print('\ngetter dan setter untuk __armor:')
print(sniper.__dict__)
print('getter__armor: ', sniper.armor)

sniper.armor = 50
print(sniper.__dict__)
print('setter__armor: ', sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)