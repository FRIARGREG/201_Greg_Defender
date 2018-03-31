
class person():
    ##  every person has the following stats:
    def __init__(self,
                 character_race,
                 character_class,
                 equipped_armour,
                 equipped_lefthand,
                 equipped_righthand,
                 power,
                 speed,
                 name):
        # let's inherit some objects first
        self.character_race = character_race
        self.cha_class = character_class ## profession object
        self.equipped_righthand = equipped_righthand ##  weapon object
        self.equipped_lefthand = equipped_lefthand ##  weapon or shield object
        self.equipped_armour = equipped_armour ##  armour object
        self.cha_level = 1
        
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
