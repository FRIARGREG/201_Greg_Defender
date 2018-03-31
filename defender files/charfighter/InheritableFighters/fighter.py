# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:45:42 2018

@author: Friar Gregarious
"""

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
import os
import dna
import functions
import person

assert os.path.basename(__file__) != '__main__.py'

from random import randint, choice


############## Be all you can be
class fighter(person):
    ### CHARACTER INITIAL VITALS
    def __init__(self, mywins = 0, myloses = 0, dna=None, name="blank", hp=0):
        person.__init__(self, dna, name, hp)
        self.ac = self.calc_ac()        
        self.wins = mywins
        self.loses = myloses       
        self.equipped = {}

    ### STANDARD INFO PRINT
    def report(self):
        self.prints += 1
        print("Fighter: %s AC: %s  HP: %s." % (self.name, self.ac, self.hp))

    ### returns sum of all currently equipped armours
    def calc_ac(self):
        current_ac = 10
# =============================================================================
#         for item_worn in self.equipped:
#             if self.equipped[item_worn].type == "armour":
#                 current_ac += item_worn.ac_value
#         current_ac += int(round(self.attribute["dex"]/10,1))
# =============================================================================
        return current_ac

    ### TAKE A SWING AT 'EM
    def attack(self, target):
        myattack = randint(1,20)
        message , result = target.defend(myattack)
        if result > 0:
            thistring = "%s hit target for %s HP. " + message
            print( thistring % (self.name, result) )
        else:
            thistring = "%s misses target. " + message
            print( thistring % self.name)

    ### DID I GET HIT AND AM I STILL ALIVE?
    def defend(self, attack):
        if attack > self.ac:
            damage = randint(1,3)
            self.hp -= damage
            if self.hp <= 0:
                self.dead = True
                message = ("%s is dead." % self.name)
                self.die()
            else:
                message = ("%s was hit and has %s HP remaining." % (self.name, self.hp))
            return message, damage
        else:
            message = ("%s avoided attack with %s HP's." % (self.name, self.hp))
            return message, 0

    def die(self):
        pass

    ### PICK A TARGET THAT IS NOT SELF
    def chooseTarget(self, available_targets=[]):
        templist = []
        newTarget = ""
        for item in available_targets:
            if item != self.name:
                templist.append(item)
        print(templist)
        if len(templist) == 1:
            newTarget = templist[0]
        elif len(templist) < 1:
            print("templist is not populated")
        else:
            newTarget = choice(templist)
        #print("Attacker: %s Target: %s" % (self.name, newTarget) )
        return newTarget



def main():
    ## this is a great place to enter test code of my module that
    ## I don't want to run when I'm actually using the software.
    print("%s is being run as %s" % (__file__,__name__))

    
    TODD = build_fighter("Todd")
    JODD = build_fighter("Jodd")
    
    JODD.attack(TODD)


    

## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'
    main()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)
