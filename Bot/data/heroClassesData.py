def сharacterAttributes(hp, damage, agility, armor):
    newClass = {}
    newClass['hp'] = hp           #жизнь
    newClass['damage'] = damage   #урон
    newClass['agility'] = agility #уклонение
    newClass['mana'] = mana       #запас маны
    return newClass

'''
Base Attributes:
hp = 80
damage = 40
agility = 5
mana = 50
'''
heroClasses = {
    'knight': сharacterAttributes(100, 50, 10, 10),
    'bard': сharacterAttributes(30, 100, 50, 10),
    'mage': 'маг',
    'thief': 'вор',
    'archer': 'лучник',
    'atronah': 'атронах', # обладает повышенным запасом маны, но не может её восстанавливать.
    'alchemist': 'алхимик',
    'potholer': 'спелеолог', # нужен в основном при походе в пещеры, может использоваться для поиска руд.
    'nomad': 'кочевник',
    'jaeger': 'егерь',
    'barbarian': 'варвар',
    'mercenary': 'наемник'    
}
"""
todo:
  1. Array heros name in this module
  2. In module run.py create class Game & make def genRandomCharackter
"""
