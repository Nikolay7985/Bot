def createClassData(hp, damage, agility, armor):
    newClass = {}
    newClass['hp'] = hp#жизнь
    newClass['damage'] = damage#урон
    newClass['agility'] = agility#увертливость
    newClass['armor'] = armor#броня
    return newClass

heroClasses = {
    'knight': createClassData(100, 50, 10, 60),
    'madman': createClassData(30, 100, 50, 10),    
}
"""
todo:
  1. Array heros name in this module
  2. In module run.py create class Game & make def genRandomCharackter
"""
