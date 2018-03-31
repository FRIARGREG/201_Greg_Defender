# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 17:11:12 2018

@author: Friar Gregarious

Every human has 23 sets of dna pairs. I will represent these with a dictionary 
of tuples.

update 
"""


from random import randint, choice
import sqlite3

class DNA(object):
    def __init__(self, genes=[], heritage=[], mutateRate=0.01):
        """ The following are class attributes """
        DNA.mutateRate = mutateRate
        DNA.genomelength = 23

        """ The following are instance attributes """
        self.fitness = 0.0
        self.genes = genes
        if len(genes) == 0:
            self.genes = newChromo(DNA.genomelength)
        self.mbti = newPersonality(self.genes)
        self.heritage = heritage
    
    def heredity(self, partner):
        sperm, egg, offspring = [], [], {}
        
        """ Build the Sperm half of the child DNA """
        for pair in partner.genes:
            mutateMe = randint(0,1000)/1000
            if mutateMe <= self.mutateRate and int(pair) > 3:
                sperm.append( newChar() )
            elif mutateMe <= self.mutateRate and int(pair) <= 3:
                sperm.append( choice(partner.genes[pair]) + randint(-5,5) )
            else:
                sperm.append( choice(partner.genes[pair]) )
        
        """ Build the Egg half of the child DNA """
        for pair in self.genes:
            mutateMe = randint(0,1000)/1000
            if mutateMe <= self.mutateRate and int(pair) > 3:
                egg.append(newChar())
            elif mutateMe <= self.mutateRate and int(pair) <= 3:
                egg.append( choice(partner.genes[pair]) + randint(-5,5) )
            else:
                egg.append(choice(self.genes[pair]))

        """ put the Child's DNA together """
        for index in range(self.genomelength):
            offspring[index] = ( sperm[index], egg[index] )

        """ record child's genetic heritage """
        childheritage = self.heritage
        if len(childheritage) >=4:
            while len(childheritage) > 2:
                childheritage.pop(0)

            childheritage.append(self.id)
            childheritage.append(partner.id)
            
        return DNA(genes=offspring, 
                   mutateRate=self.mutateRate, 
                   heritage=childheritage)
        
    def report(self):
        temp = self.mbti + "\n"
        for f in self.genes:
            temp += str(self.genes[f])+"\n"
        print(temp)


class Population(object):
    def __init__(self, population, targetphrase, maxPop, mutateRate=0.01):
        """ The following are class attributes """
        Population.target = targetphrase
        Population.mutateRate = mutateRate
        Population.maxPop = maxPop
        Population.genelength = len(targetphrase)
        Population.maxFit = self.genelength ** 2
        """ The following are instance attributes """
        self.pop = population
        self.malepool = []
        self.femalepool = []
        self.finished = False

    def selection(self):
        fits=[1]        
        for x in self.pop:
            fit, viable = x.getFit(self.target, avg(fits), max(fits))
            fits.append(fit)
            if fit/x.genelength == 1 or x.fitness == self.maxFit:
                self.finished = True
                #x.report()
                break
            elif viable:
                for i in range(fit):
                    if x.gender == "male":
                        self.malepool.append(x)
                    else:
                        self.femalepool.append(x)
            #x.report()
            ## random grab
            for x in range(int((viable/3))):
                self.mpool.append(choice(self.pop))
            
    def matetherest(self):
        if len(self.malepool) >= 1 and len(self.femalepool) >= 1:
            while len(self.pop) <= self.maxPop:
                dad = choice(self.malepool)
                mom = choice(self.femalepool)
                self.pop.append(mom.heredity(dad))
        else:
            self.firstFill()
        self.malepool.clear()
        self.femalepool.clear()

class World(object):
    def __init__(self):
        self.populations = []








def testmyAI():
    print("*****************************************************************************************************")    
    names = [
            

    def makemyparents(parent, israndom=True):
        thislist = {}
        dnalength = 23
        for x in range(dnalength):
            if x <= 3 and parent == "M":
                thislist[x] = ( 10, 90 )
            elif x <= 3 and parent == "F":
                thislist[x] = ( 40, 60 )
            else:
                if israndom:
                    thislist[x] = ( newChar(), newChar() )
                
                else:
                    temp = parent + ("00" + str(x))[-2:]
                    thislist[x] = (  temp + "a", temp + "b" )

        PARENT = DNA(genes=thislist)
        if parent == "M": ## mother
            PARENT.gender = "female"
        if parent == "F": ## father
            PARENT.gender = "male"

        PARENT.mbti = newPersonality(PARENT.genes, verbose=True)
        PARENT.report()
        return PARENT
    """ the body """
    thispop = {}
        
    print("MOTHER")
    MOTHER = makemyparents("M")
        
    print("FATHER")
    FATHER = makemyparents("F")
    
    manpool = {}
    
    firstgen = {}
    secondgen = {}
    thirdgen = {}
    
    for i in names:
        firstgen[i] = (MOTHER.heredity(FATHER))


    for i in firstgen:
        if firstgen[i].gender == "male":
            manpool.append(firstgen[i])
            firstgen[i].remove()
            

    for i in names:
        if secondgen[i].gender == "female":
            
            thirdgen[i] = (secondgen[i].heredity())
    
    
    
    
    
    for item in thispop:
        print(" ************************************* " )
        print(item)
        thispop[item].report()
    print("*****************************************************************************************************")



if __name__ == "__main__":
    testmyAI()
