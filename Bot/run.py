"""
Здесь будет происходить самое главное
"""
from data.heroClassesData import heroClasses
from classes.hero import Hero

class Game():
    def __init__(self):
        """
        а если быть совсем точным, то здесь
        """
        hero = Hero('Alex', 'knight')
        print(hero)
    
Game()
