#!/usr/bin/env python3

# this file contains objects and functions used by main

import random
from operator import attrgetter 
import crayons


# for adjustments to movement passed on a con check
mov_adjust_vals = {
    'Success-Crit': 1,
    'Success-Reg' : 0,
    'Fail'        : -1
}

# displays for map
map_symbols = {
    'empty' : ' =',
    'pit'   : 'o=',
    'cliff' : '|=',
    'hill'  : '/='
}
    

def rolldie(die):
    return(random.randint(1, die))


# take a skill rating, rolls 1-100 randomly, and returns Success/Fail if roll <= skill, crit if 1/5 of skill
def skillcheck(skillrating):
    skillroll = (rolldie(100))
    if (skillroll <= skillrating/5): 
        return ('Success-Crit')
    elif (skillroll <= skillrating):
        return('Success-Reg')
    else:
        return('Fail')


# set pursuers one beginning of map, in ascending mp order, then the headstart area is empty, then place pursues
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

        if badguy.mp > last_mp:
            empty_position += 1
            last_mp = badguy.mp

        badguy.position = empty_position

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
    # returns True if there is still someone left to chase, False otherwise
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
        elif r[1] == 'magenta':
            print(crayons.magenta (r[0]))
        else:
            print(r[0])


def printmap(mapitems):
    for i in mapitems:
        i.display()


def printintro(creatures, mapitems, roundcount):
    print ('\nStarting stats...\n')

    for creature in creatures:
        creature.hi()

    print('\n')
    printheader(roundcount)
    printmap(mapitems)
    print('\n')

    for creature in creatures:
        creature.display()
    print('\n')


def runchase(creatures, mapitems):
    caughtcount = 0
    escapedcount = 0
    roundcount = 0
    lastposition = len(mapitems) - 1

    printintro(creatures, mapitems, roundcount)

    while ischaseactive(creatures):
        roundcount += 1
        printheader(roundcount)

        printmap(mapitems)
        print('')

        roundsummary = []

        for creature in creatures:
            current_mp = creature.mp

            while (current_mp > 0 and creature.status == 'running'):

                if creature.ispursuer:

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
                    
                    if creature.status == 'running' and not ischaseactive(creatures):
                        roundsummary.append([f'{creature.symbol} - {creature.name} gives up the chase', 'yellow'])
                        creature.status = 'Gives up'


                # could be capturing or gives up by now, so no move
                if creature.status != 'running':
                    continue

                nextlocation = mapitems[creature.position + 1]

                if nextlocation.skill == 'none':
                    current_mp -= 1
                    creature.position += 1
                    roundsummary.append([f'{creature.symbol} - {creature.name} advances in {nextlocation.name}', 'blue'])

                # skill checks to pass obstacles
                elif nextlocation.skill == 'climb':
                    current_mp -= 1

                    if skillcheck(creature.climb) != 'Fail':
                        creature.position += 1
                        roundsummary.append([f'{creature.symbol} - {creature.name} deftly climbs {nextlocation.contenttype}', 'blue'])
                    else:
                        roundsummary.append([f'{creature.symbol} - {creature.name} falls from {nextlocation.contenttype}', 'magenta'])

                elif nextlocation.skill == 'con':
                    current_mp -= 1

                    if skillcheck(creature.con) != 'Fail':
                        creature.position += 1
                        roundsummary.append([f'{creature.symbol} - {creature.name} runs up {nextlocation.contenttype}', 'blue'])
                    else:
                        roundsummary.append([f'{creature.symbol} - {creature.name} fails going up {nextlocation.contenttype}', 'magenta'])

                elif nextlocation.skill == 'jump':
                    current_mp -= 1

                    if skillcheck(creature.jump) != 'Fail':
                        creature.position += 1
                        roundsummary.append([f'{creature.symbol} - {creature.name} jumps {nextlocation.contenttype}', 'blue'])
                    else:
                        roundsummary.append([f'{creature.symbol} - {creature.name} fails to jump {nextlocation.contenttype}', 'magenta'])

                if creature.position >= lastposition and not creature.ispursuer:
                    creature.status = 'escaped'
                    escapedcount += 1
                    roundsummary.append([f'{creature.symbol} - {creature.name} escapes', 'green'])

            creature.display()

        displayroundsummary(roundsummary)

    print('*' * 50, 'Summary', '*' * 50)
    print(f'\n\nEscaped: {escapedcount}, Caught: {caughtcount}\n\n')
    for creature in creatures:
        creature.hi()
class Creature:

    def __init__(self, name, mov, con, dex, luck, jump, climb, ispursuer, symbol):
        self.name = name
        # game stats common to monsters and characters 
        self.mov = mov              # movement rate
        self.con = con              # constitution 
        self.dex = dex              # dexterity
        self.luck = luck
        self.jump = jump
        self.climb = climb
        self.ispursuer = ispursuer  # True if chasing, False if chased
        self.mov = mov              # movement rate
        self.symbol = symbol        # symbol for map
        self.status = 'running' 
        self.position = -1          # position on map, based on mp
        self.mp = -1                # how many actions per round, based on mov_adjusted compared to other values in chase
        self.mov_adjusted = -1      # mov either decreased or increased based on con check

    def calc_mov_adjusted(self):
        self.mov_adjusted = self.mov + (mov_adjust_vals[skillcheck(self.con)])


    def display(self):
        for r in range(self.position):
            print(' .', end='')
        print(f' {self.symbol}')

    def hi(self):
        print(f'{self.name}:\nmov: {self.mov}, con: {self.con}, dex: {self.dex}, luck: {self.luck}, mp: {self.mp}, mov_adjusted: {self.mov_adjusted}, position: {self.position}, status: {self.status}\n')


class MapContents():
    def __init__(self, name, contenttype, skill):
        self.name = name
        self.contenttype = contenttype
        self.skill = skill

    def display(self):
        print(map_symbols[self.contenttype], end='')

    def hi(self):
        print(f'Name: {self.name}, ContentType: {self.contenttype}, Skill: {self.skill}')
