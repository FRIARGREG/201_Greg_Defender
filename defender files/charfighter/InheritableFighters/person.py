# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:29:10 2018

@author: friar

THIS FILE CONTAINS THE OBJECT FOR CHARACTERS IN THE GAME


"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 07:45:42 2018

@author: friar
"""

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
import os
import dna
import functions

assert os.path.basename(__file__) != '__main__.py'

from random import randint, choice


class person(object):
    def __init__(self, DNA=None, name="blank", hp=0):

        """ every person has their own DNA object """
#        self.dna = DNA_object().newChromo() if DNA == None else DNA
        self.name = name
        self.filename = "%s.txt" % self.name
        self.prints = 0
        self.hp = hp
        self.ac = None
        self.ac = self.calc_ac()
        self.deadoralive = False
        #self.equipped = { "armour":skin(), "right_hand":stick() }

    def calc_ac(self):
        pass

