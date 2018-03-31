# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:07:26 2018

@author: friar

"""

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
import os
assert os.path.basename(__file__) != '__main__.py'

class thing(object):
    def __init__(self, **kwargs):
        """ the root of all things is existance """
        self.weight = kwargs.get('weight', 0.0)
        self.volume = kwargs.get('volume', 0)
        self.encumberance = self.calc_encumbrance()
        
    def calc_encumbrance(self):
        """ encumberance is how difficult a thing is carry. """
        return self.weight * self.volume * 2


class carryer(thing):
    """ a thing for carrying stuff. makes life easier """
    def __init__(self, burnable=None, meltable=None, weight=0.0,
                 volume=0.0, capacity=0, max_cap=0):
        thing.__init__(self, burnable, meltable, weight, volume)
        self.container = True
        self.contains = []
        self.capacity = 0
        self.max_capacity = self.calc_maxCap() if max_cap == 0 else 0
            
    def calc_encumbrance(self, verbose=False):
        """ calculates and can return encumberance """
        self.encumberance = self.weight * self.volume * 1.5
        if verbose:
            return self.encumberance
        
    def calc_maxCap(self, verbose = False):
        """ calculates and can return the maximum capacity for a container """
        self.max_capacity = self.volume
        if verbose:
            return self.max_capacity
        
    def put_stuff_in(self, stuff=False, verbose = False):
        """ for adding things to a container 

        """
        msg = ""
        toomuch = self.capacity + stuff.volume > self.max_capacity
        # ===================================================
        ### 
        if ( stuff != False ):
            if ( not toomuch ): 
                self.contains.append( stuff )
                self.capacity += stuff.volume
                msg = "Added to container"
            else:
                msg = "did not add item"
        # ===================================================
        ### recalculating current capacity
        self.capacity = 0
        for item in self.contains:
            if self.capacity + stuff.volume >= self.max_capacity:
                msg += " cannot add any more stuff to container"
            else:
                self.capacity += item.volume
        # ===================================================
        ### only prints if asked too 
        if verbose:
            print(msg)
    
class food(thing):
    def __init__(self, meltable=None, weight=0, volume=0, foodvalue = 0.0 ):
        """ food items can give characters nutrients or health """
        thing.__init__(self, meltable, weight, volume)
        self.burnable = True
        self.foodvalue = foodvalue





def main():
    ## this is a great place to enter test code of my module that
    ## I don't want to run when I'm actually using the software.
    print("%s is being run as %s" % (__file__,__name__))
    
    basket = carryer()
    basket.weight = 1
    basket.volume = 10
    basket.encumberance = basket.calc_encumbrance()
    basket.container = True
    basket.calc_maxCap()
    
    apple = food()
    apple.burnable = True
    apple.weight = 1
    apple.volume = 1
    apple.foodvalue = 1
    apple.encumberance = apple.calc_encumbrance()
    

    for x in range(25):
        basket.put_stuff_in(apple, verbose=True)
        print("Basket contains %s of %s percent capacity." % ( len(basket.contains), 
                                                       ( basket.capacity / basket.max_capacity )
                                                       ) )
    
    




## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'
    main()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)



