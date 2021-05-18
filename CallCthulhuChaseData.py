#!/usr/bin/env python3
import CallCthulhuChaseObjects as cobj

def createdata():

    headstart = 3


    creatures = []

    creatures.append(cobj.Creature(name = 'Scooby',        mov = 9, con = 50, dex = 75, luck = 90, jump = 60, climb = 20, ispursuer = False, symbol = 's'))
    creatures.append(cobj.Creature(name = 'Shaggy',        mov = 8, con = 40, dex = 65, luck = 80, jump = 40, climb = 30, ispursuer = False, symbol = 'h'))
    creatures.append(cobj.Creature(name = 'Velma',         mov = 7, con = 40, dex = 45, luck = 70, jump = 30, climb = 35, ispursuer = False, symbol = 'v'))
    creatures.append(cobj.Creature(name = 'Daphne',        mov = 8, con = 70, dex = 75, luck = 60, jump = 65, climb = 75, ispursuer = False, symbol = 'd'))
    creatures.append(cobj.Creature(name = 'Fred',          mov = 8, con = 90, dex = 65, luck = 60, jump = 60, climb = 65, ispursuer = False, symbol = 'f'))
    
    creatures.append(cobj.Creature(name = 'Zombie',        mov = 6, con = 80, dex = 35, luck = 40, jump = 10, climb = 20, ispursuer = True,  symbol = 'Z'))
    creatures.append(cobj.Creature(name = 'Mummy',         mov = 6, con = 80, dex = 35, luck = 40, jump = 10, climb = 20, ispursuer = True,  symbol = 'M'))
    creatures.append(cobj.Creature(name = 'Ghoul',         mov = 9, con = 65, dex = 65, luck = 40, jump = 32, climb = 32, ispursuer = True,  symbol = 'G'))
    creatures.append(cobj.Creature(name = 'Deep One',      mov = 8, con = 50, dex = 55, luck = 30, jump = 22, climb = 22, ispursuer = True,  symbol = 'D'))
    creatures.append(cobj.Creature(name = 'Dark Young',    mov = 8, con = 80, dex = 85, luck = 30, jump = 40, climb = 40, ispursuer = True,  symbol = 'Y'))
    

    mapitems = []

    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Grassland', contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Craig',     contenttype = 'hill',  skill = 'con'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Craig',     contenttype = 'cliff', skill = 'climb'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'pit',   skill = 'jump'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'empty', skill = 'none'))
    mapitems.append(cobj.MapContents(name = 'Jungle',    contenttype = 'pit',   skill = 'jump'))

    return(creatures, mapitems, headstart)
