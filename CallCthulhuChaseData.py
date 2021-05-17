#!/usr/bin/env python3
#from CallCthulhuChaseObjects import *
#from CallCthulhuChaseObjects import Creature
import CallCthulhuChaseObjects as cobj

def createdata():

    headstart = 2


    creatures = []

    creatures.append(cobj.Creature(name = 'Byakee', mov = 9, con = 50, dex = 1, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'B'))
    creatures.append(cobj.Creature(name = 'Big Deep One', mov = 6, con = 50, dex = 10, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'D'))
    creatures.append(cobj.Creature(name = 'Deep One', mov = 8, con = 60, dex = 30, luck = 20, jump = 50, climb = 50, ispursuer = True, symbol = 'd'))
    creatures.append(cobj.Creature(name = 'Drexler Logan', mov = 8, con = 40, dex = 50, luck = 20, jump = 50, climb = 50, ispursuer = False, symbol = '1'))
    creatures.append(cobj.Creature(name = 'Slow Logan', mov = 8, con = 99, dex = 20, luck = 50, jump = 50, climb = 50, ispursuer = False, symbol = '2'))
#    creatures.sort(key=attrgetter('dex', 'con'), reverse = True)


    mapitems = []

    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'pit',   skill = 'jump'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle', contenttype = 'pit',   skill = 'jump'))

    return(creatures, mapitems, headstart)
