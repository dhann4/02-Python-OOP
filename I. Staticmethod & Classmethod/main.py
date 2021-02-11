class Hero:

    # Private Class Variable
    __jumlah = 0

    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah

    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah

    # Static Method (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2(): # tidak bisa di mengambil argument dari class maupun objek
        return Hero.__jumlah
        '''
        perlu di ingat. Untuk Static Method ini, jika nama class nya di ganti maka harus di ganti juga dengan nama class yang baru
        jika nama class nya adalah Hero, di return nya juga memakai nama si Hero.__Jumlah menjadi = Hero.__Jumlah
        jika nama class nya kita ganti menjadi Pahlawan, di return nya juga harus di ganti dengan Pahlawan.__Jumlah menjadi = Pahlawan.__Jumlah

        dan ini sangat tidak fleksibel
        '''

    # bisa di anggap sebagai objek dan bisa di anggap sebagai class
    @classmethod
    def getJumlah3(cls): # mempunyai argument
        return cls.__jumlah
        '''
        berbeda dengan static method.
        Untuk Class Method ini, jika nama class nya di ganti tidak perlu di ganti lagi mengikuti nama class yang baru, karena dalam class method
        jika class di ganti maka class method akan otomatis mengikuti nama si class nya.
        contoh :
        jika nama class nya kita ubah dari Hero menjadi Pahlawan, maka class method akan mengikuti class yang namanya di ubah
        dari Hero ke Pahlawan.
        
        Karena dalam class method memakai format (cls) atau (class), jadi sangat memudahkan untuk mengganti nama class
        tanpa harus khawatir si return nya akan error karena nama class berbeda dari yang sebelum nya
                
        dan ini sangat fleksibel
        '''


sniper = Hero('Sniper')
print(Hero.getJumlah2())
rikimaru = Hero('Rikimaru')
print(rikimaru.getJumlah2())

pudge = Hero('Pudge')
print(Hero.getJumlah3())
print(pudge.getJumlah3())