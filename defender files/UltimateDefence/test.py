
from chargen import *
from defence import *

Fildegar = person(character_race=Elf,
                  character_class=Soldier,
                  equipped_armour=SplintMail,
                  equipped_lefthand=WoodHeavy,
                  equipped_righthand=LongSword,
                  power=10,
                  speed=10,
                  name="Fildegar")

Rudnick = person(character_race=Dwarf,
                  character_class=Soldier,
                  equipped_armour=PlateMail,
                  equipped_lefthand=WoodHeavy,
                  equipped_righthand=GreatAxe,
                  power=10,
                  speed=10,
                  name="Rudnick")

Fildegar.experience += 6000
Rudnick.experience += 6000

Fildegar.LevelMeUp()
Rudnick.LevelMeUp()

Rudnick.Describe()
Fildegar.Describe()

battle(Fildegar, Rudnick)
