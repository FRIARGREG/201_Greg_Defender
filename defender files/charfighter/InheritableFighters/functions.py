# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:51:43 2018

@author: friar

this module hold all the functions used in my genetics experiments

"""
from random import randint, choice
import dna
import fighter

def getFit(me, compare, average, highest):
    skor = 0
    for i in range(me.genelength):
        if me.genes[i] == compare[i]:
            skor += 1
    fitness = skor**2
    viable = fitness > int(average + ((highest-average)/2))
    return fitness, viable

def isRelated(me, partner):
    related = False
    for x in me.heritage:
        for y in partner.heritage:
            if x == y:
                related = True
    return related

def avg(str2avg):
    """ returns average of numbers in a list """
    a = 0
    for i in str2avg:
        a += i
    return a/len(str2avg)

def buildtarget(text):
    tarlist = []
    for i in text:
        tarlist.append(text(i))
    return text, tarlist

def firstFill(thisPop):
    thisPop.pop.clear()
    thisPop.malepool.clear()        
    thisPop.femalepool.clear()        
    i = 0
    while i <= len(thisPop.maxPop):
        i += 1
        genestring = []
        x = 0
        while x <= len(thisPop.genelength):
            x += 1
            genestring.append(newGene())                
        child = dna.DNA( genestring , thisPop.mutateRate)
        thisPop.pop.append(child)                

def build_fighter(give_name):
    a = fighter.fighter(dna=newChromo(15), name=give_name , hp=25)
    return a
    
    
    