#!/usr/bin/env python3
import random

class Creature:
    def __init__(self, name, mov, con, jump, climb, creaturetype):
        self.name = name
        # game stats common to monsters and characters 
        self.mov = mov      # movement rate
        self.con = con      # constitution 
        self.jump = jump
        self.climb = climb
        self.creaturetype = creaturetype

class MapContents():
    def __init__(self, name, contenttype, skill):
        self.name = name
        self.contenttype = contenttype
        self.skill = skill

    def hi(self):
        print(f'Name: {self.name}, ContentType: {self.contenttype}, Skill: {self.skill}')


def main():
    monster1 = Creature(name = 'Deep One', mov = 7, con = 50, jump = 50, climb = 50, creaturetype = 'monster')

    maplist = []
    maplist.append(MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    x=maplist[0]
    x.hi()

main()




