class Hero: # dinamakan Super Class

    def __init__(self, name, health):
        self.name = name
        self.health = health

class Hero_Intellegent(Hero): # dinamakan Sub Class dari Super Class
    pass

class Hero_Strength(Hero): # dinamakan Sub Class dari Super Class
    pass

lina = Hero('Lina', 100) # dari Super Class Hero
techies = Hero_Intellegent('Techies', 50) # dari Sub Class Hero Intellegent
axe = Hero_Strength('Axe', 200) # dari Sub Class Hero Strength

print(lina.name)
print(techies.name)
print(axe.name)