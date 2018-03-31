# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:26:35 2018

@author: friar
"""

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


if __name__ == "__main__":
    from random import randint, choice
    from functions import *
