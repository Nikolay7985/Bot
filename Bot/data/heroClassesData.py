def createClassData(hp, damage, agility, armor):
    newClass = {}
    newClass['hp'] = hp#жизнь
    newClass['damage'] = damage#урон
    newClass['agility'] = agility#увертливость
    newClass['armor'] = armor#броня
    return newClass

heroClasses = {
    'knight': [100, 50, 10, 60],
    'madman': [30, 100, 50, 10]
}

#another_dict = {"number":23, 2: True, "my_list":[1,2,3]}

print(heroClasses)
