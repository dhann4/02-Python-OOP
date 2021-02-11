class Hero:

    def __init__(self, name, health, attackPower):
        # membuat semua attribute menjadi private
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    # melakukan perhitungan di belakang layar
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaibaru):
        self.__attPower = nilaibaru

# awal dari game
sniper = Hero('Sniper', 50, 5)

# game berjalan
# print(sniper.__name) akan error, jadi jika begini, itu tidak akan bisa
print(sniper.getName()) # jika begini akan muncul nama dari hero nya yaitu Sniper
print(sniper.getHealth())
sniper.diserang(5)
print(sniper.getHealth())

