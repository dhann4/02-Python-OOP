# Game Sederhana

class Hero:

    def __init__(self, name, health, attackPower, armor):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armor = armor

    def attack(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name)
        lawan.deffend(self, self.attackPower)

    def deffend(self, lawan, attackPower_lawan):
        print(self.name + ' Diserang ' + lawan.name)
        attack_diterima = attackPower_lawan/self.armor
        print('Attack di terima : ' + str(attack_diterima))
        self.health -= attack_diterima
        print('Darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('Sniper', 100, 10, 5)
rikimaru = Hero('Rikimaru', 100, 20, 10)

sniper.attack(rikimaru)
print("\n")
rikimaru.attack(sniper)

print("\n")
rikimaru.attack(sniper)

print("\n")
rikimaru.attack(sniper)

print("\n")
rikimaru.attack(sniper)


