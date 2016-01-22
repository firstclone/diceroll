import random
from sys import exit

def help():
    print 'Functions:'
    print 'Roll---choose number of dice, number of'
    print '       sides and bonus.'
    print 'Top----choose total number of dice, number of'
    print '       sides and how many dice to use.'
    print 'Char---rolls for skills for a new character.'
    print 'Check--rolls for an ability check.'
    print 'Save---rolls for a death-saving throw.'
    print 'Help---show functions available.'
    print 'Exit---closes the program.'
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: help()
    
def roll():
    dice = int(raw_input('Number of dice: '))
    sides = int(raw_input('Number of sides: '))
    bonus = raw_input('Bonus: ')
    if bonus == '':
        bonus = '0'
    bonus = int(bonus)
    total = 0
    while dice > 0:
        total = total + random.randint(1,sides)
        dice = dice - 1
    final = total + bonus
    print 'Total:', final
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: roll()
        
def top():
    all_dice = int(raw_input('Total number of dice rolled: '))
    top_dice = int(raw_input('Number of dice kept: '))
    sides = int(raw_input('Number of sides: '))
    bonus = raw_input('Bonus: ')
    if bonus == '':
        bonus = '0'
    bonus = int(bonus)
    while all_dice < top_dice:
        print 'ERROR: Total dice rolled fewer than dice kept.'
        all_dice = int(raw_input('Total number of dice rolled: '))
        top_dice = int(raw_input('Number of dice kept: '))
        sides = int(raw_input('Number of sides: '))
        bonus = raw_input('Bonus: ')
        if bonus == '':
            bonus = '0'
        bonus = int(bonus)
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = bonus
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print top_rolls
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: top()

def char():
    all_dice = 4
    top_dice = 3
    sides = 6
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Str:', top_rolls
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Dex:', top_rolls
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Con:', top_rolls
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Int:', top_rolls
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Wis:', top_rolls
    dicey = {}
    for i in range(0, all_dice):
        dicey[i] = random.randint(1,sides)
    rolls = dicey.values()
    rolls = sorted(rolls)[::-1]
    top_rolls = 0
    for x in range (top_dice):
        top_rolls = top_rolls + rolls[x]
    print 'Cha:', top_rolls
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: char()
    
def check():
    abscore = int(raw_input('Ability Score: '))
    proflvl = int(raw_input('Proficiency Level: '))
    adv = raw_input('Advantage(a), Disadvantage(d): ').lower()
    roll = 0
    abil = {1: -5, 2: -4, 3: -4, 4: -3, 5: -3, 6: -2, 7: -2, 8: -1, 9: -1, 10: 0, 11: 0, 12: 1, 13: 1, 14: 2, 15: 2, 16: 3, 17: 3, 18: 4, 19: 4, 20: 5, 21: 5, 22: 6, 23: 6, 24: 7, 25: 7, 26: 8, 27: 8, 28: 9, 29: 9, 30: 10}
    prof = {0: 0, 1: 2, 2: 2, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 3, 9: 4, 10: 4, 11: 4, 12: 4, 13: 5, 14: 5, 15: 5, 16: 5, 17: 6, 18: 6, 19: 6, 20: 6}
    if adv == 'a':
        roll = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll2 > roll:
            roll = roll2
    elif adv == 'd':
        roll = random.randint(1,20)
        roll2 = random.randint(1,20)
        if roll2 < roll:
            roll = roll2
    else:
        roll = random.randint(1,20)
    if roll == 20:
        print 'Critical Hit!'
    if roll == 1:
        print 'Critical Fail!'
    profbonus = prof.get(proflvl, 0)
    abbonus = abil.get(abscore, -5)
    score = roll + profbonus + abbonus
    print score
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: check()
	
def save():
    roll = random.randint(1,20)
    if roll == 1:
        print 'Double Fail!'
    if roll > 1 and roll < 10:
        print 'Fail'
    if roll > 9 and roll < 20:
        print 'Success'
    if roll == 20:
        print 'Critical Success! +1 HP'
    run = raw_input('Enter Function: ').lower().strip()
    if run == 'exit':
        raise SystemExit
    else:
        try: functions.get(run)()
        except: save()
        
functions = {'help': help, 'roll': roll, 'top': top, 'char': char, 'check': check, 'save': save}
run = None
help()
