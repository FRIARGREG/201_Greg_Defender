# First I need to import some standard stuff
from random import randint



# Armours equiped by Characters
class armour():
    def __init__(self,
                 armour_type,
                 armour_name,
                 armour_protection,
                 armour_weight):
        self.armour_type = armour_type
        self.armour_name = armour_name
        self.armour_protection = armour_protection
        self.armour_weight = armour_weight

# Shields equiped by Characters
class shield():
    def __init__(self,
                 shield_name,
                 shield_type,
                 deflect,
                 damage_type,
                 bash_damage,
                 attack_speed,
                 attack_range,
                 hands):
        self.shield_name = shield_name
        self.shield_type = shield_type
        self.deflect = deflect
        self.damage_type = damage_type
        self.bash_damage = bash_damage
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.hands = hands

        if self.damage_type != "none":
            self.attack_descriptor = "attempts a shield bash"
        else:
            self.attack_descriptor = "this shield is not for attacking"

# Weapons equiped by Characters
class weapon():
    def __init__(self,
                 weapon_name,
                 weapon_type,
                 damage_type,
                 weapon_damage,
                 weapon_speed,
                 weapon_range,
                 hands):
        self.weapon_type = weapon_type
        self.weapon_name = weapon_name
        self.weapon_damage = weapon_damage
        self.weapon_dmg_type = damage_type
        self.weapon_speed = weapon_speed
        self.hands = hands

        if weapon_type == "range":
            self.attack_descriptor = "shoots at"
        else:
            self.attack_descriptor = "swings at"

# races make minor adjustments to stats and special abilities
class race():
    def __init__(self,
                 race,
                 fortitude,
                 reflexes,
                 willpower,
                 spell_resistance,
                 energy_resistance,
                 damage_reduction,
                 adj_str,
                 adj_dex,
                 adj_con,
                 adj_int,
                 adj_wis,
                 adj_cha):
        self.race = race
        self.fortitude = fortitude
        self.reflexes = reflexes
        self.willpower = willpower
        self.spell_resistance = spell_resistance
        self.energy_resistance = energy_resistance
        self.damage_reduction = damage_reduction
        self.adj_str = adj_str
        self.adj_dex = adj_dex
        self.adj_con = adj_con
        self.adj_int = adj_int
        self.adj_wis = adj_wis
        self.adj_cha = adj_cha



# Professions dictate starting stats and special abilities
class profession():
    def __init__(self,
                 title,
                 prof_type, ## is this a supporter, assaulter or spellcaster?
                 fortitude,
                 reflexes,
                 willpower,
                 spell_resistance,
                 energy_resistance,
                 damage_reduction):
        self.title = title
        self.fortitude = fortitude
        self.reflexes = reflexes
        self.willpower = willpower
        self.spell_resistance = spell_resistance
        self.energy_resistance = energy_resistance
        self.damage_reduction = damage_reduction
        
        self.combat_points_per_level = 5
        self.skill_points_per_level = 2
        self.magic_points_per_level = 2

        if prof_type == "assaulter": ## assaulters are Soldiers, warriors, thugs, barbarrians & weapon masters
            self.base_health = 10
            self.base_str = 5
            self.base_dex = 3
            self.base_con = 5
            self.base_int = 1
            self.base_wis = 3
            self.base_cha = 1
        elif prof_type == "support": ## support includes rogues, scouts, paladins, rangers & experts 
            self.base_health = 7
            self.base_str = 1
            self.base_dex = 5
            self.base_con = 3
            self.base_int = 1
            self.base_wis = 5
            self.base_cha = 3
        else: ## spell casters are the only others including Clerics, Wizards, Sorcerors, Shamen & Elementalists
            self.base_health = 4
            self.base_str = 1
            self.base_dex = 3
            self.base_con = 1
            self.base_int = 5
            self.base_wis = 5
            self.base_cha = 3
            

class person():
    ##  every person has the following stats:
    def __init__(self,
                 name,
                 character_race,
                 character_class,
                 equipped_armour,
                 equipped_lefthand,
                 equipped_righthand,
                 power,
                 speed,
                 level=1,
                 total_experience=0):
        
        # let's inherit some objects first
        self.character_race = character_race
        self.cha_class = character_class ## profession object
        self.equipped_righthand = equipped_righthand ##  weapon object
        self.equipped_lefthand = equipped_lefthand ##  weapon or shield object
        self.equipped_armour = equipped_armour ##  armour object
        self.cha_level = level ## defaults to level 1 if not supplied.
        
        # now we assign the values we were given
        self.name = name # what my mamma named me
        self.power = power # internal measure of spirit/magic/mana... whatev's
        self.speed = speed # movement rate
        self.experience = 0 # current XP for Current Level
        self.experience_total = 0 # sum of experience in point form
        self.alive = True # am I dead yet? or it can read as animated_corpse, alive means still active

        self.combat_points = self.cha_class.combat_points_per_level
        self.skill_points = self.cha_class.skill_points_per_level
        self.magic_points = self.cha_class.magic_points_per_level

        self.strength = self.cha_class.base_str + self.character_race.adj_str
        self.dexterity = self.cha_class.base_dex + self.character_race.adj_dex
        self.constitution = self.cha_class.base_con + self.character_race.adj_con
        self.intelligence = self.cha_class.base_int + self.character_race.adj_int
        self.wisdom = self.cha_class.base_wis + self.character_race.adj_wis
        self.charisma = self.cha_class.base_cha + self.character_race.adj_cha

        self.fortitude = self.cha_class.fortitude + self.character_race.fortitude
        self.reflexes = self.cha_class.reflexes + self.character_race.reflexes
        self.willpower = self.cha_class.willpower + self.character_race.willpower

        self.spell_resistance = self.cha_class.spell_resistance + self.character_race.spell_resistance
        self.energy_resistance = self.cha_class.energy_resistance + self.character_race.energy_resistance
        self.damage_reduction = self.cha_class.damage_reduction + self.character_race.damage_reduction

        self.initiative = self.dexterity + self.equipped_righthand.weapon_speed - self.equipped_armour.armour_weight
        self.hit_points = self.cha_class.base_health + self.constitution
            
        self.reInit()

        ## save hard values to database
        db = sqlite3.connect("defence.sqlite")
        c = db.cursor()
        c.execute("INSERT INTO characters VALUES (" + self.name, self.character_race.,      +");")


    def reInit(self):
        # Here we calculate attributes from those given values
        self.hit_points = (self.constitution + self.cha_class.base_health) * self.cha_level
        self.movement = self.speed + self.dexterity

    # method for determining initiative for this character this round
    def GoesOn(self):
        self.initiative = self.dexterity + self.equipped_righthand.weapon_speed - self.equipped_armour.armour_weight
        return randint(1,20) + self.initiative

    # this method is for attacking
    def attack(self, target):
        my_attack, isCrit = self.calculate_attack(self.equipped_righthand.weapon_type)
        target_defence = target.calculate_defence(self.equipped_righthand.weapon_type)
        describe_attack = (self.name
                           + " " + self.equipped_righthand.attack_descriptor
                           + " " + target.name)

        if self.equipped_righthand.hands == 2:
            dmg_mod = 1.5
        else:
            dmg_mod = 1

        damage_roll = randint(1,self.equipped_righthand.weapon_damage)
        dmg_taken = (int(dmg_mod * (self.strength))
                     + (damage_roll * isCrit)
                     - target.damage_reduction)
        
        if my_attack > target_defence:
            self.experience += int(dmg_taken/3)
            self.dealDamage(target,dmg_taken)
            if isCrit == 2:
                describe_attack += (" and makes a CRITICAL HIT for a MAX damage of "
                                    + str(dmg_taken))
            else:
                describe_attack += (" and HITS for "
                                    + str(dmg_taken)
                                    + " points of damage!")
        else:
            describe_attack += " and missed."
            self.experience -= 1
        print(describe_attack)
       

    # helper method manage health & death
    def dealDamage(self, damaged_guy, ammount_of_damage):
        damaged_guy.hit_points -= ammount_of_damage

        if damaged_guy.hit_points in range(1,10):
            print(damaged_guy.name, "is in critical condition!")
        elif damaged_guy.hit_points <= 0:
            xpearned = int(damaged_guy.experience/10)
            print(damaged_guy.name, "DIES and", self.name, "earns",
                  xpearned, "XP!")
            self.experience += xpearned
            self.LevelMeUp
            print(self.name, "now has", self.experience, "Experience!!")
            damaged_guy.alive = False
    
    # This calculates the attack of this character
    def calculate_attack(self, attack_type):
        att_roll = randint(1,20)
        if att_roll == 20:
            critical_strike = 2
        else:
            critical_strike = 1
        
        if attack_type == "range": # ranged attack
            return (self.dexterity + att_roll), critical_strike
        elif attack_type == "melee": # melee attack
            return (self.strength + att_roll), critical_strike
        else: # for magic when I figure it out
            return 0, critical_strike
        

    # This calculates the defence of this character
    def calculate_defence(self, attack_type):
        baseAC = self.equipped_armour.armour_protection + self.equipped_lefthand.deflect
        
        if attack_type == "ranged": # Do I Dodge?
            return baseAC
        elif attack_type == "melee": # or Do I Block it?
            return baseAC
        else: #this is the case of a magic attack
            return baseAC + self.spell_resistance + self.energy_resistance

    # helper method to change some of the equipment around
    def equip_item(self, itemtype, itemname):
        if itemtype == "weapon":
            self.equipped_righthand = itemname
            if itemname.hands > 1:
                self.equipped_lefthand = LeftHandEmpty
        if itemtype == "armour":
            self.equipped_armour = itemname
        if itemtype == "shield":
            self.equipped_lefthand = itemname

    # Helper method to level-up character (eventually can multiclass!!)
    def LevelMeUp(self,verbose=False):
        levelme = self.HowMuchCompleted() >= 1
        while levelme:
            if verbose:
                print(self.name, "Levels UP!!!")
            self.experience -= self.NextLevelRequirement()
            self.experience_total += self.NextLevelRequirement()
            self.cha_level += 1 # here is the official level up to trickle down to all the stats
            if (self.cha_level % 5 == 0):
                self.strength += 1
                self.dexterity += 1
                self.constitution += 1
                self.intelligence += 1
                self.wisdom += 1
                self.charisma += 1

            self.fortitude += self.cha_class.fortitude
            self.reflexes += self.cha_class.reflexes
            self.willpower += self.cha_class.willpower

            self.spell_resistance += self.cha_class.spell_resistance
            self.energy_resistance += self.cha_class.energy_resistance
            self.damage_reduction += self.cha_class.damage_reduction

            self.hit_points += 1 + randint(self.constitution, self.constitution+self.cha_class.base_health)

            self.reInit()
            levelme = self.HowMuchCompleted() >= 1 ## changes the flag to decide if we level up again.

    # Helper method returns the required XP to level up
    def NextLevelRequirement(self):
        return self.cha_level * 100

    # This helper method returns an integer of the percentage for the completion
    # of the current level. ie current=200xp/required=400xp = return of 50
    def HowMuchCompleted(self):
        return int(100*(self.experience/self.NextLevelRequirement()))

    # Helper method for viewing current stats of character
    def Describe(self):
        print("***************************************")
        print(self.name + " is a level " + str(self.cha_level) + " "
              + self.character_race.race + self.cha_class.title
              + " with " + str(self.HowMuchCompleted()) + " percent of this level completed")
        print("for a total of", self.experience + self.experience_total, "XP!!")
        print("He's wearing", self.equipped_armour.armour_name, "and carrying a",
              self.equipped_righthand.weapon_name, "and a",
              self.equipped_lefthand.shield_name, "shield")
        print("His Attributes and Saves are:")

        myA = "Strength     " + ("    " + str(self.strength))[-4:]
        myB = "  Fortitude        " + ("    " + str(self.fortitude))[-4:]
        print(myA + myB)
        myA = "Dexterity    " + ("    " + str(self.dexterity))[-4:]
        myB = "  Reflexes         " + ("    " + str(self.reflexes))[-4:]
        print(myA + myB)
        myA = "Constitution " + ("    " + str(self.constitution))[-4:]
        myB = "  Willpower        " + ("    " + str(self.willpower))[-4:]
        print(myA + myB)
        myA = "Intelligence " + ("    " + str(self.intelligence))[-4:]
        myB = "  Spell Resist     " + ("    " + str(self.spell_resistance))[-4:]
        print(myA + myB)
        myA = "Wisdom       " + ("    " + str(self.wisdom))[-4:]
        myB = "  Energy Resist    " + ("    " + str(self.energy_resistance))[-4:]
        print(myA + myB)
        myA = "Charisma     " + ("    " + str(self.charisma))[-4:]
        myB = "  Damage Reduction " + ("    " + str(self.damage_reduction))[-4:]
        print(myA + myB)
        

### THESE FUNCTIONS ARE FOR BATTLE TESTING
    


def battle(guyA,guyB):
    print("######### BATTLE #########")

    this_round = 0
    while guyA.alive and guyB.alive:
        this_round += 1
        guyA_Init = guyA.GoesOn()
        guyB_Init = guyB.GoesOn()
        
        print ("-------------------")
        print ("Round:", this_round)
        print(("            " + guyA.name)[-19:] + ("             " + guyB.name)[-10:])
        print(("    Init    " + str(guyA_Init))[-19:] + ("             " + str(guyB_Init))[-10:])
        print(("    Health  " + str(guyA.hit_points))[-19:] + ("             " + str(guyB.hit_points))[-10:])

        if guyA_Init > guyB_Init:
            if guyA.alive:
                guyA.attack(guyB)
            if guyB.alive:
                guyB.attack(guyA)
        elif guyA_Init < guyB_Init:
            if guyB.alive:
                guyB.attack(guyA)
            if guyA.alive:
                guyA.attack(guyB)

    print("Battle Over!")






"""
##--------------------------------------------------------------------
## characters for this battle
## Joram is a melee sword fighter wearing chainmail
Joram = Person(name = "Joram", health = 50, speed = 3,
               power = 5, experience = 5,
               equipped_weapon=sword, equipped_armour=platemail)

## reggy is a ranged bow fighter wearing leather armour
Reggy = Person(name = "Reggy", health = 50, speed = 3,
               power = 5, experience = 5, alive = True,
               equipped_weapon=longbow, equipped_armour=leather)

##--------------------------------------------------------------------
def print_stats(rnd):
    print ("#############################################")
    print ("Round:", rnd)


##--------------------------------------------------------------------
## FIGHT!!!!

print ("Joram has", Joram.health,
       "health and is wielding a", Joram.weapon.weapon_name)
print ("Reggy has", Reggy.health,
       "health and is wielding a", Reggy.weapon.weapon_name)
print ("###################")
this_round = 0
while Joram.alive and Reggy.alive:
    this_round += 1
    print_stats(this_round)

    Jo_Init = Joram.initiative + random.randint(1,10)
    Rg_Init = Reggy.initiative + random.randint(1,10)
    print("Joram Init =", Jo_Init, "vs Reggy Init =", Rg_Init)
    if Jo_Init > Rg_Init:

        if Joram.alive:
            Joram.attack(Reggy)
        if Reggy.alive:
            Reggy.attack(Joram)
    elif Rg_Init > Jo_Init:
        if Reggy.alive:
            Reggy.attack(Joram)
        if Joram.alive:
            Joram.attack(Reggy)


print("Battle Over!")

"""







##def defineWeaponDmg(min_value, max_value):
##    possiblemagic = random.randint(1,100)
##    basedamage = random.randint(min_value, max_value)
##    magicdamage = 0
##    ismagic = False
##    print("Base Damage =", basedamage)
##    if possiblemagic > 90:
##        magicdamage = (possiblemagic - 90)
##        print("Magic Damage =", magicdamage)
##        ismagic = True
##    else:
##        magicdamage = 0
##    return basedamage + magicdamage, ismagic
##
##isthisweaponmagic = False
##while isthisweaponmagic == False:
##    thisweapon, isthisweaponmagic = defineWeaponDmg(1,10)
##    print ("Total Damage =", thisweapon)
