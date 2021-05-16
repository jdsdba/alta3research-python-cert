#!/usr/bin/env python3
import random

mov_adjust_vals = {
    'Success-Crit': 1,
    'Success-Reg' : 0,
    'Fail'        : -1
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

def calculate_mp (creatures):
    lowest_mov = min(c.mov_adjusted for c in creatures)

    for creature in creatures:
        creature.mp = creature.mov_adjusted - lowest_mov + 1
        creature.hi()

class Creature:

    mov_adjust_vals = {
        'Success-Crit': 1,
        'Success-Reg' : 0,
        'Fail'        : -1
    }

    def __init__(self, name, mov, con, dex, luck, jump, climb, creaturetype):
        self.name = name
        # game stats common to monsters and characters 
        self.mov = mov      # movement rate
        self.con = con      # constitution 
        self.dex = dex
        self.luck = luck
        self.jump = jump
        self.climb = climb
        self.creaturetype = creaturetype
        self.position = -1
        self.mp = -1
        self.mov_adjusted = self.mov + (mov_adjust_vals[skillcheck(self.con)])
        self.mov = mov      # movement rate

    def hi(self):
        print(f'Name: {self.name}, mov: {self.mov}, con: {self.con}, dex: {self.dex}, luck: {self.luck}, mp: {self.mp}, mov_adjusted: {self.mov_adjusted}')

class MapContents():
    def __init__(self, name, contenttype, skill):
        self.name = name
        self.contenttype = contenttype
        self.skill = skill

    def hi(self):
        print(f'Name: {self.name}, ContentType: {self.contenttype}, Skill: {self.skill}')


def main():
    creatures = []
    creatures.append(Creature(name = 'Deep One', mov = 7, con = 60, dex = 30, luck = 20, jump = 50, climb = 50, creaturetype = 'monster'))
    creatures.append(Creature(name = 'Drexler Logan', mov = 8, con = 40, dex = 30, luck = 20, jump = 50, climb = 50, creaturetype = 'player'))
    creatures.append(Creature(name = 'Slow  Logan', mov = 6, con = 99, dex = 30, luck = 20, jump = 50, climb = 50, creaturetype = 'player'))

    maplist = []
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))

    x=maplist[0]
    #x.hi()
    calculate_mp(creatures)

main()




