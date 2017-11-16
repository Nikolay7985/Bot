from data.heroClassesData import heroClasses

class Hero(object):
    """docstring for Hero"""
    def __init__(self, name, heroClass):
        self.name = name
        self.heroClassStr = heroClass
        self.heroClass = heroClasses[heroClass]
        self.hp = self.heroClass['hp']
        self.damage = self.heroClass['damage']
        self.agility = self.heroClass['agility']
        self.armor = self.heroClass['armor']
    
    def __str__(self):
        return self.printHero()
    
    def printHero(self):
        dictEnRus = {
            'knight': 'рыцарь',
            'madman': 'безумец'
        }
        return 'Привет, меня зовут ' + self.name + ' и я ' + dictEnRus[self.heroClassStr] + str(self.hp)
