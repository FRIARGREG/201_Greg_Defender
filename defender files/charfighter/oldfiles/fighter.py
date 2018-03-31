# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:45:42 2018

@author: friar
"""

############## Be all you can be
class fighter(object):
    ### CHARACTER INITIAL VITALS
    def __init__(self, myname, mywins = 0, myloses = 0):
        self.name = myname
        self.filename = "%s.txt" % self.name
        self.prints = 0
        self.hp = randint(10,25)
        self.ac = randint(7,12)
        self.dead = False
        self.wins = mywins
        self.loses = myloses

    ### STANDARD INFO PRINT
    def printme(self):
        self.prints += 1
        print("Fighter: %s AC: %s  HP: %s." % (self.name, self.ac, self.hp))

    ### TAKE A SWING AT 'EM
    def attack(self, target):
        myattack = randint(1,20)
        message , result = combatant[target].defend(myattack)
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
                combatant.pop(self.name)
                charlist.remove(self.name)
            else:
                message = ("%s was hit and has %s HP remaining." % (self.name, self.hp))
            return message, damage
        else:
            message = ("%s avoided attack with %s HP's." % (self.name, self.hp))
            return message, 0

    ### PICK A TARGET THAT IS NOT SELF
    def chooseTarget(self):
        templist = []
        newTarget = ""
        for item in charlist:
            if item != self.name:
                templist.append(item)
        print(templist)
        if len(templist) == 1:
            newTarget = templist[0]
        elif len(templist) < 1:
            print("templist is not populated")
        else:
            newTarget = random.choice(templist)
        #print("Attacker: %s Target: %s" % (self.name, newTarget) )
        return newTarget

    ## this needs to save to a record in the game db. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def saveChar(self, targetfile = ""):
##        with open(self.filename, "w") as f:
##            f.write("%s,%s,%s,%s,%s,%s" % (self.name, self.ac, self.hp, self.dead, self.wins, self.loses))
        with 
