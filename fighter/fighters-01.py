from random import choice, randint
from Fighter_Class import *
from functions import *




class CONS:
    CONS.verbose = True
    tcbo1 = False
    map_max = 10
    players = {}
    roundcount = 0
    starting_locs = []
    fighter_Pool = ['Fighter 1', 'Fighter 2', 'Fighter 3']
    grid = build_grid(map_max)

def setup():
    print('@@@@@@@@@@@@@@@@@@@@   testing setup() function') if CONS.verbose else None
    ''' define all characters, the map, starting positions and weapons locs '''
    ## make fighters list. This is optional, defaults exist in the CONS class
    get_fighters('fighterfile.txt')

    ## this is where we initialize the fighters
    for x in CONS.fighter_Pool:
        CONS.players[x] = person(x)
    for x in CONS.fighter_Pool:
        CONS.players[x].pick_target()

    ## last part, I'm going to delete old namespaces
    del CONS.starting_locs

def main():
    log = open('battle_file.txt', 'w') 
#    with open('battle_file.txt', 'w') as log:

    ## The main program for fighting
    msg = '############### FIGHT!!! ###############\n'
    print(msg, end='')
    log.write(msg + '\n')
    print(type(log))
    ## as long as there are at least 2 fighters
    while not CONS.tcbo1:
        CONS.roundcount += 1                    ## this is the new round
        msg = '**** Round ' + str(CONS.roundcount) + '\n'   ## print round data
        print(msg, end='')
        log.write(msg)
   
        for char in CONS.fighter_Pool:               ## for each character  still standing
            guy = CONS.players[char]
            if guy.target != None:
                msg = str(guy.attack(CONS.players[guy.target])) + '\n'
                print(msg, end='')
                log.write(msg)
                print('@@@@@@@@@@@@@@@@@@@@@ testing - attack loop')


        CONS.tcbo1 = (len(CONS.fighter_Pool) <= 1)
        if CONS.tcbo1:
            print('@@@@@@@@@@@@@@@@@@@@@ testing exit logic')

            winner = CONS.fighter_Pool.pop()
            msg = "############### " + str(winner) + " wins the Battle ###############\n"
            print(msg, end='')
            log.write(msg)
    log.write('end of battle prog.\n')
    log.close()

setup()
main()
print('Program End')
