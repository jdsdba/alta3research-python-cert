#!/usr/bin/env python3

import CallCthulhuChaseObjects as cco
import CallCthulhuChaseData as ccd

def main():

    (creatures, mapitems, headstart) = ccd.createdata()

    cco.initchase(creatures, headstart)
    cco.runchase(creatures, mapitems)

if __name__ == "__main__":
    main()




