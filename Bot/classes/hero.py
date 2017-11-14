from data.heroClassesData import heroClasses

class Hero(object):
    """docstring for Hero"""
    def __init__(self, name, heroClass):
        self.name = name
        self.heroClassStr = heroClass
        self.heroClass = heroClasses['heroClass']
        self.hp = self.heroClass['hp']
        self.damage = self.heroClass['damage']
        self.agility = self.heroClass['agility']
        self.armor = self.heroClass['armor']

    def printHero(self):
        dictEnRus = {
            'knight': 'рыцарь',
            'madman': 'безумец'
        }
        print('Привет, меня зовут ' + self.name + ' и я ' + dictEnRus[self.heroClassStr])



hero = Hero()
hero.printHero()
