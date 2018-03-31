from random import choice, randint

################################################3
################################################3
###
###  PERSON CLASS
###
################################################3
################################################3

class person():
    def __init__(self, name):
        """  """
        self.name = name
        self.strength = randint(5, 7)
        self.tohit = 0
        self.health = 10 + randint(1, 10)
        self.defence = 10 + randint(0, 5)
        self.alive = True
        self.loc = random_loc()
        self.target = None
        self.target_loc = (0, 0)
        self.visible = randint(1, 20)

    def attack(self, oponnent):
        ''' (object, object) --> str '''

        self.tohit = self.strength + randint(1, 20)
        if self.tohit > oponnent.defence:
            this_damage = damage(self.strength)
            r_msg = ("%s ( %s : %s ) ; %s ( %s : %s ) ; %s " % \
                (self.name, self.health, self.visible, oponnent.name, oponnent.health,oponnent.visible, this_damage))
            oponnent.health -= this_damage
        else:
            r_msg = ("%s (%s/%s) missed %s (%s/%s)." % (self.name, self.health, self.visible, oponnent.name, oponnent.health,oponnent.visible ))
        
        if oponnent.health <= 0:
            r_msg += '\n' + oponnent.die()
            self.pick_target()
        return r_msg

    def die(self):
        self.alive = False
        CONS.fighter_Pool.remove(self.name)
        r_msg = ('   ----> ' + self.name + ' has died.')
        for x in CONS.players:
            if CONS.players[x].target == self.name:
                CONS.players[x].pick_target()
        del CONS.players[self.name]
        return r_msg
        
    def move_to(self, new_loc):
        new_loc = args.get('new_loc', self.target_loc)
        if self.loc != new_loc:
            self.loc = determine_direction(new_loc) ## next step

    def pick_target(self):
        pick_temp = []
        for item in CONS.fighter_Pool:
            if item != self.name:
                if CONS.players[item].alive:
                    probability = [item for x in range(CONS.players[item].visible)]
                    for x in probability:
                        pick_temp.append(x)                    

        if len(pick_temp) == 0:
            self.target = None
        else:
            print('I have', len(pick_temp), 'options.')
            self.target = choice(pick_temp)


class battle():
    def __init__(self, **kwargs):
        self.combatants = kwargs.get(combatants, dict())
        self.round = 0
        



### FUNCTION FOR CALCULATING DAMAGE APPLIED TO SUCCESSFUL HITS
def damage(strength):
    return randint(1, strength)

### FUNCTION FOR BUILDING A FIGHTER FILE
def make_fighter_file():
    names = ['ANGUS',
             'BRAVE',
             'CHUCK',
             'DAVE',
             'ERICA',
             'FLORA',
             'GEORGE',]

    with open('fighterfile.txt', 'w') as save_file:
        for name in names:
            save_file.write(name + '\n')

### FUNCTION GETS FIGHTERS FROM FIGHTER FILE
def get_fighters(filename):
    CONS.fighter_Pool = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            cname = line[:-1]
            CONS.fighter_Pool.append(cname)

### FUNCTION GENERATES A RANDOM LOCATION ON GRID
def random_loc():
    still_looking = True
    count = 0
    while still_looking and count < 10000:
        count += 1
        this_loc = (randint(0, CONS.map_max), randint(0, CONS.map_max))
        if this_loc not in CONS.starting_locs:
            CONS.starting_locs.append(this_loc)
            still_looking = not still_looking
            return this_loc
    return "Too Many Attempts"

### FUNCTION BUILDS MAIN GRID
def build_grid(grid_max):
    my_range = range(0, int(grid_max))
    temp_grid = [[" " for y in my_range] for x in my_range]
    return temp_grid

################################################3
## CONSTANTS USED THROUGHT THE PROGRAM
################################################3
class CONS:
    verbose = True
    tcbo1 = False
    map_max = 10
    players = {}
    roundcount = 0
    starting_locs = []
    fighter_Pool = ['Fighter 1', 'Fighter 2', 'Fighter 3']
    grid = build_grid(map_max)

################################################3
### FUNCTION SETS UP BATTLES FOR TESTING THE PERSON CLASS
################################################3
def setup():
    ''' define all characters, the map, starting positions and weapons locs '''
    ## make fighters list. This is optional, defaults exist in the CONS class
    try:
        get_fighters('fighterfile.txt')
    except:
        make_fighter_file()
        get_fighters('fighterfile.txt')

    ## this is where we initialize the fighters
    for x in CONS.fighter_Pool:
        CONS.players[x] = person(x)
    for x in CONS.fighter_Pool:
        CONS.players[x].pick_target()

    ## last part, I'm going to delete old namespaces
    del CONS.starting_locs

################################################3
### MAIN FUNCTION FOR TESTING PERSON CLASS
################################################3
def main():
    with open('battle_file.txt', 'w+') as log:

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

            CONS.tcbo1 = (len(CONS.fighter_Pool) <= 1)
            if CONS.tcbo1:
                winner = CONS.fighter_Pool.pop()
                msg = "############### " + str(winner) + " wins the Battle ###############\n"
                print(msg, end='')
                log.write(msg)
        log.write('end of battle prog.\n')




################################################3
setup()
main()
print('Program End')
