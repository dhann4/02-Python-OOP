class Hero:
    # Class Variable
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # Method tanpa return / Void Function
    def siapa(self):
        print("Namaku adalah " + self.name)

    # Method dengan argumen tanpa return
    def healthUp(self,up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Sniper", 100, 10, 5)
hero2 = Hero("Mario Bros", 98, 5, 10)

hero1.siapa()
hero1.healthUp(10)

print(hero1.health)
print(hero1.getHealth())