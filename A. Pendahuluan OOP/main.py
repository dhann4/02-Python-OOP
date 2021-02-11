class Hero(): # template
    pass


hero1 = Hero() # object / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Sniper'
hero1.health = 100

hero2.name = 'Sven'
hero2.health = 200

hero3.name = 'Ucup'
hero3.health = 1000

print(hero1)
print(hero1.__dict__)
print(hero1.name)

