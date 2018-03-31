"""
This is my attempt to read & write class info to and from SQL file.
"""
from random import randint, choice 
import os
import fighter

combatant = {}
charlist = []

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
assert os.path.basename(__file__) != '__main__.py'



############## There Can Be Only One
def tcbo1(fighters):
    countAlive = 0
    for thischar in fighters:
        if not combatant[thischar].dead:
            countAlive += 1
    if countAlive > 1:
        print(countAlive)
        print("keep fighting!!")
        return False
    else:
        print("Fight Over!")
        return True

### only runs while testing this module
def main():
    ############## List the fighters
    with open("chars.txt", "r") as x:
        charlist = x.readline().split(",")
    print(charlist)
        #["Greg", "Fran", "Dave", "Sara", "Leon", "Kate", "Mike", "Rhea"]
        
    
    for item in charlist:
        combatant[item] = fighter(item)
        combatant[item].printme()
        combatant[item].saveChar()

    ############## FIGHT!!!
    while not tcbo1(combatant):
        for attacker in charlist:
            target = combatant[attacker].chooseTarget()
            combatant[attacker].attack(target)
            
    combatant[charlist[0]].printme()


## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'

    main()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)

