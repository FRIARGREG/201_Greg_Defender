# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:33:18 2018
@author: Friar Gregarious


"""

## new template for my code
import os, datetime
from dna import living_dna

# =============================================================================
# date_time = datetime.datetime.now()
# moment = date_time.time()
# current_check = datetime.datetime.minute - moment
# 
# =============================================================================


class basic_exist_thing(object):
    """ the root of all things is existance """
    def __init__(self, **kwargs):
        """ the root of all things is existance 
        x = carbonbasedlife.basic_exist_thing(height=1.83, mass=2500, length=3, width=2)
        x.calc_volume()
        : 10.98
        x.calc_encumbrance()
        : 54900.0
        
        """
        # =====================================================================
        # this is the parent for all objects in this world
        #      * all objects have physical attibutes and simple methods of
        #        behaviour like gravity and magnetics
        #      * to make things far simpler and to bite my thumb at the U.S.
        #        all measurements will be in metric. so there Mr. Trump.
        #
        #   stuff to add Vectors, Forces, Oscillation
        #
        # =====================================================================
        self.mass = kwargs.get('mass', 0.0)

        self.height = kwargs.get('height', 0.0)
        self.length = kwargs.get('length', 0.0)
        self.width = kwargs.get('width', 0.0)

        self.vector = kwargs.get('vector', (0, 0))
        self.vector_magnitude = 0
        self.vector_speed = 0
        
        self.volume = kwargs.get('volume', self.calc_volume())
        self.encumberance = kwargs.get('encumberance', self.calc_encumbrance())

    def calc_volume(self):
        """ volume is how much space a thing displaces """
        return self.height * self.width * self.length

    def calc_encumbrance(self):
        """ encumberance is how difficult a thing is carry. """
        return self.mass * self.volume * 2

# =============================================================================
# nodes are the items which manage the experiences into what 
# the living thing has learned or feels. I have started 3 basic
# nodes based on a root node. the root node is the template
# while the other nodes have more specific uses.
# =============================================================================

class root_motivation(object):
    """ all emotions, thoughts, skills and talents will come from this """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.modifiers = kwargs.get('modifiers', self.init_modifiers())
        self.current_value = kwargs.get('starting_value', 0)
        if count(self.modifiers) > 0:
            self.current_value = calc_current_value()

    def init_modifiers(self):
        self.modifiers['fear'] = {'danger':(-5,0),
                                  'injury':(-5,0),
                                  'darkness':(-5,0),
                                  'fire':(-5,0),
                                  'magic':(-5,0),
                                  'weather':(-5,0),
                                  'safety':(1,None)}
        self.modifiers['hunger'] = {'eaten':(5,0),
                                    'pregnant':(-2,0),
                                    'injury':(-2,0),
                                    'exertion':(-5,0)}
        self.modifiers['arousal'] = {'danger':(0,0),
                                     'danger':(0,0),
                                     'danger':(0,0),
                                     'danger':(0,0)}
        self.modifiers['exhaustion'] = {'danger':(0,0),
                                        'danger':(0,0),
                                        'danger':(0,0),
                                        'danger':(0,0)}

    def calc_current_value(self):
        """ 1) sum up all the current temporary/variable modifiers and apply to 
        current value. step 2) Then add all the permanent effects. """
        ## STEP 1: APPLY TEMPORARY FACTORS AND ADJUST PERIOD
        total_variable_modification = 0
        for modifier in self.modifiers:
            modify_value, modify_period = self.modifiers[modifier]
            if modify_period > 0:
                total_variable_modification += modify_value
                self.modifiers[modifier] = (modify_value, modify_period -1)
        return total_variable_modification + self.total_permanent_effects

# =============================================================================
#     def get_permanent_modifiers(self):
#         """ runs at init and anytime permanent modifiers change """
#         ## STEP 2: APPLY PERMANENT FACTORS FROM PERSON
#         total_permanent_effects = 0
#         person_perm_modifiers = kwargs.get('person_perm_modifiers', dict())
#         if self.name in person_perm_modifiers:
#             ## DICT("NAME OF AFFECTOR" : (VALUE TO JUMP, MIN VAL OF CURRENT, MAX VAL OF CURRENT))
#             my_value, my_min, my_max = person_perm_modifiers[self.name]
#             if self.current_value <= my_min:
#                 total_permanent_effects += my_value
#             elif self.current_value >= my_max:
#                 total_permanent_effects -= my_value
#         return total_permanent_effects
# =============================================================================


# =============================================================================
# skills will behave very similar to emotions, they have a base value, they have
# a list of modifiers, they recalc their value, they get used.
# however, when a skill gets used, it has an opportunity to improve itself.
# this improvement through use is used as the growth model for our people as
# opposed to the D20 level up through xp point model which isn't very applicable
# to a simulation like world. This is more DUNGEON SEIGE.
#  ** note (I've never seen the code for DUNGEON SEIGE so don't sue me.)
# =============================================================================

std_skill_list = ['fist_attack', 'stick_attack', 'club_attack', 'dagger_attack', 'short_sword_attack',
                  'long_sword_attack', 'great_sword_attack', 'bastard_sword_attack', 'scimitar_attack',
                  'cutlass_attack', 'hand_axe_attack', 'wood_axe_attack','battle_axe_attack', 'great_axe_attack',
                  'pole_arm_attack', 'short_spear_attack', 'long_spear_attack', 'bardiche_attack', 'javalin_attack']

def build_std_skills(skill_list):
    this_dict = {}
    for skill in skill_list:
        this_dict += dict(skill : (0, 0))
    return this_dict




character.skills = {'skill_name' : (current_lvl, xp_earned)} # of skill objects



class skill_node(object):
    """ this object represents a usable skill in the game """
    def __init__(self, **kwargs):
        self.skill_list = build_std_skills(std_skill_list)
        self.update_skills(kwargs.get('name', False))

    def update_skill(self, skill_update): # this should be a tuple
        """ updates the existing skills with the dictionary received """
        self.skill_list.update(updated_skills) ## this acts passively, nothing returned

    def use_this_skill(self, skill_to_use):
        """ did it work? if yes call learning method """
        used = True
        worked = True
        if used and worked:
            self.learn_from_use(skill_to_use)
        elif used and not worked:
            current_lvl, xp_earned = self.skill_list[skill_to_use]
            self.skill_list[skill_to_use] = (current_lvl, (xp_earned + 1))

    def learn_from_use(self, skill_used):
        """ there is a chance character will improve their skill level """
        current_lvl, xp_earned = self.skill_list[skill_used]
        
        chance_temp = xp_earned / ((skill_level + 1) * 10)
        chance_to_learn = chance_temp if (chance_temp > min_chance_to_learn) else min_chance_to_learn
        RandomRoll = randint(0,1000)/1000
        if randroll <= chance_to_learn:
            xp_earned += int(chance_to_learn - RandomRoll)

        ## do I have enough to level up this skill?
        while (xp_earned >= (current_lvl + 1) * 10):
            xp_earned -= (current_lvl + 1) * 10
            current_lvl += 1












class primitive_brain(object):
    """ all the basic primitive reactions are here """
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.motivators = ['fear', 'hunger', 'arousal', 'exhaustion']
        self.basic_instincts = {}
        for motive in motivaors:
            self.basic_instincts[motive] = root_motivation(name=motive, 
                                                           modifiers=kwargs.get('modifiers'))
                
    def assess(self):
        """ re-evaluate motivators """
# =============================================================================
#         The primitive mind is almost constantly scanning for danger,
#         and searching to fulfill it's neads like hunger, sex, sleep
# =============================================================================









# =============================================================================
# class emote_node(root_node):
#     """ I am Jack's Rage. I simmer until threatened """
#     def __init__(self, **kwargs):
#         root_node.__init__(self, kwargs)
# =============================================================================


class living_thing(basic_exist_thing):
    """ container for living_dna() this object contains the methods that all
    living creatures require which represent instincts """
    def __init__(self, **kwargs):
        """ initializing first heartbeat """
        basic_exist_thing.__init__(self)
        self.dna = kwargs.get('dna', living_dna())
        self.emotional_state = self.calc_emotional_state(first_run=True)
        self.physical_state = self.calc_physical_state(first_run=False)
        self.permanent_affectors = kwargs.get('permanent_effects', dict())

    def instinct_reproduce(self):
        """ all life feels a drive to reproduce """
        pass

    def instinct_survive(self):
        """ all life feels a drive to preserve their own existance. """
        pass

    def instinct_feed(self):
        """ all life feels hunger which also triggers survival. """
        # =====================================================================
        # this method will also handle thirst. no need to make things
        # too complicated. we're only dealing with a light simulation
        # =====================================================================
        pass

    def instinct_protect_kind(self):
        """ triggered when offspring, mate or community member is harmed """
        # =====================================================================
        # all creatures have an emotional state of balance which can (and will)
        # be affected by their environment, their own actions/inactions and the
        # actions/inactions of the creatures/people around them.
        # =====================================================================
        pass

    def calc_emotional_state(self, **kwargs):
        """ this method constantly adjusts emotional state of the creature """
        # =====================================================================
        # all creatures have an emotional state of balance which can (and will)
        # be affected by their environment, their own actions/inactions and the
        # actions/inactions of the creatures/people around them.
        # =====================================================================
        # my_state is a dictionary of lists. list[0] is always the current
        # state of this emotion, list[index>0] will contain tuples of reactions
        # this being has when it meets/experiences things & events
        first_run = kwargs.get('first_run', False)
        my_now = kwargs.get('time_called', False)
        my_state = self.calc_emotional_state

        if first_run:
            my_state = {'love' : [0],
                        'contentment' : [0],
                        'distress' : [0],
                        'frustration' : [0],
                        'fear' : [0],
                        'anger' : [0],
                        'belonging' : [0]}

        if my_now >= self.last_updated + (minutes(10)):
            self.last_updated = my_now
            for emotion in my_state:
                # time produces emotional entropy
                my_state[emotion][0] += 1 if my_state[emotion][0] < 0 else -1
                # but conditions can affect emotions over time
                if len(my_state[emotion]) >=1:
                    for affector in my_state[emotion]:
                        if affector > 0:
                            my_state[emotion][0] += my_state[emotion][affector]
        ## I may replace the integers stored in the emotion lists with an
        ## emotion_affector object.
        return my_state

    def calc_physical_state(self, **kwargs):
        """ this method constantly adjusts physical state of the creature """
        first_run = kwargs.get('first_run', False)
        my_now = kwargs.get('time_called', False)
        my_state = self.calc_physical_state

        if now() >= self.last_updated + (minutes(10)):
            self.last_updated = int(datetime.datetime.now())

        my_state = {'thirst' : [0],
                    'hunger' : [0],
                    'pain' : [0],
                    'discomfort' : [0]}
        return my_state










# =============================================================================
# This section is simply for testing purposes. if this module is run directly
#  which only happens when I want to test it, then the test_my_classes() func
#  will instantiate the classes i've created here and test their output.
# =============================================================================

def test_my_classes():
    """ for testing purposes only """
    ## this is a great place to enter test code of my module that
    ## I don't want to run when I'm actually using the software.
    print("%s is being run as %s" % (__file__, __name__))
    x = basic_exist_thing(height = 1.83,
                          mass = 2500,
                          length = 3,
                          width = 2)
    if x.calc_volume() == 10.98:
        print("basic_exist_thing passed test #1")
    if x.calc_encumbrance() == 54900.0:
        print("basic_exist_thing passed test #2")

    x = living_thing()self.dna = kwargs.get('dna', living_dna())
        self.emotional_state = self.calc_emotional_state(first_run=True)
        self.physical_state = self.calc_physical_state(first_run=False)
        self.permanent_affectors = kwargs.get('permanent_effects', dict())
    
    



## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
assert os.path.basename(__file__) != '__main__.py'

## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'
    test_my_classes()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)
