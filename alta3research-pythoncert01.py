#!/usr/bin/env python3
import random
from operator import attrgetter 

headstart = 2

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


def initchase (creatures):
    for creature in creatures:
        creature.calc_mov_adjusted()

    lowest_mov = min(c.mov_adjusted for c in creatures)

    for creature in creatures:
        # determine mp for each creature
        creature.mp = creature.mov_adjusted - lowest_mov + 1

    empty_position = 0
    for badguy in sorted(creatures, key=attrgetter('mp', 'con')): 
        if not badguy.ispursuer:
            continue
        badguy.position = empty_position
        empty_position += 1
        #badguy.hi()

    empty_position += headstart
    for goodguy in sorted(creatures, key=attrgetter('mp', 'con')): 
        if goodguy.ispursuer:
            continue
        goodguy.position = empty_position
        empty_position += 1


def ischaseactive(creatures):
    isactive = False
    for creature in creatures:
        if creature.status == 'running' and not creature.ispursuer:
            isactive = True
            break
    return(isactive)

def printheader(roundcount):
    print('*' * 50, f'Round: {roundcount}', '*' * 50, '\n')


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

        roundsummary = '\n'

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
                            roundsummary += f'{creature.symbol} - {creature.name} catches {caughtcreature.name}\n'
                            break
                        
                        remaining_pursue += 1

                    if creature.status == 'running' and remaining_pursue == 0:
                        roundsummary += f'{creature.symbol} - {creature.name} gives up the chase\n'
                        creature.status = 'Gives up'


                if creature.status != 'running':
                    continue

                nextlocation = mapitems[creature.position + 1]

                if nextlocation.skill == 'none':
                    current_mp -= 1
                    creature.position += 1
                    roundsummary += f'{creature.symbol} - {creature.name} advances\n'

                elif nextlocation.skill == 'jump':
                    current_mp -= 1

                    if skillcheck(creature.jump) != 'Fail':
                        creature.position += 1
                        roundsummary += f'{creature.symbol} - {creature.name} jumps\n'
                    else:
                        roundsummary += f'{creature.symbol} - {creature.name} fails to jump\n'

                if creature.position >= lastposition and not creature.ispursuer:
                    creature.status = 'escaped'
                    escapedcount += 1
                    roundsummary += f'{creature.symbol} - {creature.name} escapes\n'

            creature.display()

        print(roundsummary)

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


def main():

    creatures = []
    creatures.append(Creature(name = 'Byakee', mov = 9, con = 50, dex = 1, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'B'))
    creatures.append(Creature(name = 'Big Deep One', mov = 6, con = 50, dex = 10, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'D'))
    creatures.append(Creature(name = 'Deep One', mov = 8, con = 60, dex = 30, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'd'))
    creatures.append(Creature(name = 'Drexler Logan', mov = 8, con = 40, dex = 50, luck = 20, jump = 50, climb = 50, ispursuer = False, symbol = '1'))
    creatures.append(Creature(name = 'Slow Logan', mov = 8, con = 99, dex = 20, luck = 50, jump = 50, climb = 50, ispursuer = False, symbol = '2'))
    creatures.sort(key=attrgetter('dex', 'con'), reverse = True)

    mapitems = []
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'pit',   skill = 'jump'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(MapContents(name = 'Jungle', contenttype = 'pit',   skill = 'jump'))

    initchase(creatures)
    runchase(creatures, mapitems)

main()




