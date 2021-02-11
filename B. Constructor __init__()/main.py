class Hero():

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero('Sniper', 100, 10, 4)
hero2 = Hero('Mirana', 100, 15, 1)
hero3 = Hero('Ucup', 1000, 100, 0)

# memanggil nama hero
print(hero1.name)
# memanggil health hero
print(hero2.health)
# memanggil armor hero
print(hero3.armor)

# mengetahui di dalam objek nya mempunyai atribut apa saja
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)