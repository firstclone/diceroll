import random
dice = int(raw_input('Number of dice: '))
sides = int(raw_input('Number of sides: '))
bonus = int(raw_input('Bonus: '))
total = 0
while dice > 0:
    total = total + random.randint(1,sides)
    dice = dice - 1
final = total + bonus
print final
