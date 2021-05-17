#!/usr/bin/env python3
import random
from operator import attrgetter 
#from CallCthulhuChaseData.py import *
import crayons


mov_adjust_vals = {
    'Success-Crit': 1,
    'Success-Reg' : 0,
    'Fail'        : -1
}

map_symbols = {
    'empty' : ' =',
    'pit'   : 'o=',
    'cliff' : '|='
}
    

def rolldie(die):
    return(random.randint(1, die))


def skillcheck(skillrating):
    skillroll = (rolldie(100))
    if (skillroll <= skillrating/5): 
        return ('Success-Crit')
    elif (skillroll <= skillrating):
        return('Success-Reg')
    else:
        return('Fail')


def initchase (creatures, headstart):
    creatures.sort(key=attrgetter('dex', 'con'), reverse = True)

    for creature in creatures:
        creature.calc_mov_adjusted()

    lowest_mov = min(c.mov_adjusted for c in creatures)

    for creature in creatures:
        # determine mp for each creature
        creature.mp = creature.mov_adjusted - lowest_mov + 1

    lowest_mp_badguys = min(c.mp for c in creatures if c.ispursuer)
    lowest_mp_goodguys = min(c.mp for c in creatures if not c.ispursuer)

    empty_position = 0
    last_mp = lowest_mp_badguys
    for badguy in sorted(creatures, key=attrgetter('mp', 'con')): 
        if not badguy.ispursuer:
            continue
        badguy.hi()

        if badguy.mp > last_mp:
            empty_position += 1
            last_mp = badguy.mp

        badguy.position = empty_position
        badguy.hi()

    empty_position += headstart
    last_mp = lowest_mp_goodguys
    for goodguy in sorted(creatures, key=attrgetter('mp', 'con')): 
        if goodguy.ispursuer:
            continue

        if goodguy.mp > last_mp:
            empty_position += 1
            last_mp = goodguy.mp

        goodguy.position = empty_position


def ischaseactive(creatures):
    isactive = False
    for creature in creatures:
        if creature.status == 'running' and not creature.ispursuer:
            isactive = True
            break
    return(isactive)

def printheader(roundcount):
    print('*' * 50, f'Round: {roundcount}', '*' * 50, '\n')

def displayroundsummary(roundsummary):
    for r in roundsummary:
        if r[1] == 'red':
            print(crayons.red (r[0]))
        elif r[1] == 'green':
            print(crayons.green (r[0]))
        elif r[1] == 'yellow':
            print(crayons.yellow (r[0]))
        elif r[1] == 'blue':
            print(crayons.blue (r[0]))
        else:
            print(r[0])


def runchase(creatures, mapitems):
    caughtcount = 0
    escapedcount = 0
    roundcount = 0
    printheader(roundcount)

    lastposition = len(mapitems) - 1

    for i in mapitems:
        i.display()
    print('\n')

    for creature in creatures:
        creature.display()
    print('\n')

    while ischaseactive(creatures):
        roundcount += 1
        printheader(roundcount)

        for i in mapitems:
            i.display()
        print('')

        roundsummary = []

        for creature in creatures:
            #creature.hi()
            current_mp = creature.mp

            while (current_mp > 0 and creature.status == 'running'):

                if creature.ispursuer:
                    remaining_pursue = 0

                    for caughtcreature in sorted(creatures, key=attrgetter('luck')):
                        if creature == caughtcreature:
                            continue
                        if caughtcreature.ispursuer:
                            continue
                        if caughtcreature.status != 'running':
                            continue
                        if caughtcreature.position == creature.position:
                            current_mp -= 1
                            caughtcreature.status = 'captured'
                            creature.status = 'capturing'
                            caughtcount += 1
                            roundsummary.append([f'{creature.symbol} - {creature.name} catches {caughtcreature.name}', 'red'])
                            break
                        
                        remaining_pursue += 1

                    if creature.status == 'running' and remaining_pursue == 0:
                        roundsummary.append([f'{creature.symbol} - {creature.name} gives up the chase', 'yellow'])
                        creature.status = 'Gives up'


                if creature.status != 'running':
                    continue

                nextlocation = mapitems[creature.position + 1]

                if nextlocation.skill == 'none':
                    current_mp -= 1
                    creature.position += 1
                    roundsummary.append([f'{creature.symbol} - {creature.name} advances', 'blue'])

                elif nextlocation.skill == 'jump':
                    current_mp -= 1

                    if skillcheck(creature.jump) != 'Fail':
                        creature.position += 1
                        roundsummary.append([f'{creature.symbol} - {creature.name} jumps', 'blue'])
                    else:
                        roundsummary.append([f'{creature.symbol} - {creature.name} fails to jump', 'blue'])

                if creature.position >= lastposition and not creature.ispursuer:
                    creature.status = 'escaped'
                    escapedcount += 1
                    roundsummary.append([f'{creature.symbol} - {creature.name} escapes', 'green'])

            creature.display()

        displayroundsummary(roundsummary)

    print('*' * 50, 'Summary', '*' * 50)
    print(f'\n\nEscaped: {escapedcount}, Caught: {caughtcount}')


class Creature:

    def __init__(self, name, mov, con, dex, luck, jump, climb, ispursuer, symbol):
        self.name = name
        # game stats common to monsters and characters 
        self.mov = mov      # movement rate
        self.con = con      # constitution 
        self.dex = dex
        self.luck = luck
        self.jump = jump
        self.climb = climb
        self.ispursuer = ispursuer
        self.mov = mov      # movement rate
        self.symbol = symbol
        self.status = 'running'
        self.position = -1
        self.mp = -1
        self.mov_adjusted = -1

    def calc_mov_adjusted(self):
        self.mov_adjusted = self.mov + (mov_adjust_vals[skillcheck(self.con)])


    def display(self):
        for r in range(self.position):
            print(' .', end='')
        print(f' {self.symbol}')

    def hi(self):
        print(f'Name: {self.name}, mov: {self.mov}, con: {self.con}, dex: {self.dex}, luck: {self.luck}, mp: {self.mp}, mov_adjusted: {self.mov_adjusted}, position: {self.position}, status: {self.status}')


class MapContents():
    def __init__(self, name, contenttype, skill):
        self.name = name
        self.contenttype = contenttype
        self.skill = skill

    def display(self):
        print(map_symbols[self.contenttype], end='')

    def hi(self):
        print(f'Name: {self.name}, ContentType: {self.contenttype}, Skill: {self.skill}')
