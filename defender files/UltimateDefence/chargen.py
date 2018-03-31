## First I need to import some standard stuff
import random, sqlite3
#from defence import *
## list of names
db = sqlite3.connect("defence.sqlite")
c = db.cursor()

names = ["Roger",       "Mike",     "Regdar",   "Adulo",    "Briva",    "Chaliu",   "Dross",
         "Encarnacion", "Frodulo",  "Grusk",    "Haviar",   "Inglais",  "Juss",     "Klundik",
         "Lumio",       "Morch",    "Nunn",     "Opha",     "Plaug",    "Jenny",    "Frederick",
         "Reginald",    "Bianca",   "Fitz",     "Harry",    "Margaret", "Elizabeth","Victoria",
         "William",     "Charles",  "George",   "Phillip",  "Regimin",  "Lauras",   "Lina",
         "Remy",        "Lumia",    "Retch",    "Inglemire","Raja",     "Greg",     "Unff",
         "J'adoon",     "Julia",    "Ragnar",   "John",     "O'Leary",  "Fraggle", "Soon"]

##--------------------------------------------------------------------
## list of races available
### race(race fort ref will s_resist e_resist dam_reduce adj_str adj_dex adj_con adj_int adj_wis adj_cha

races =  [(1,    "Elf",    -1,  1,  0,  1,  0,  0, -1,  1, -1,  1,  0,  0),
          (2,    "Human",   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
          (3,    "Orc",     1,  0, -1,  0,  0,  0,  1,  0,  1, -1, -1,  0),
          (4,    "Dwarf",   0, -1,  1,  0,  0,  1,  0,  0,  1,  0,  1, -2),
          (5,    "Halfling",0,  1, -1,  0,  1,  0, -2,  1, -1,  0,  1,  1),
          (6,    "Gnome",  -1,  0,  1,  0,  1,  0, -2,  1, -1,  1,  0,  1)]

c.execute("DROP TABLE IF EXISTS races")
c.execute("CREATE TABLE races (\
          'id' INTEGER PRIMARY KEY, \
          'race' TEXT, \
          'fort' INTEGER, \
          'ref' INTEGER, \
          'will' INTEGER, \
          's_resist' INTEGER, \
          'e_resist' INTEGER, \
          'dam_reduce' INTEGER, \
          'adj_str' INTEGER, \
          'adj_dex' INTEGER, \
          'adj_con' INTEGER, \
          'adj_int' INTEGER, \
          'adj_wis' INTEGER, \
          'adj_cha' INTEGER);")
c.executemany("INSERT INTO races VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (races))
db.commit()


##--------------------------------------------------------------------
## list of character classes available
classes = [(1, "Soldier",     "assaulter",    2,  1,  1,  0,  0,  0),
           (2, "Warrior",     "assaulter",    2,  0,  2,  0,  0,  0),
           (3, "Thug",        "assaulter",    2,  2,  0,  0,  0,  0),
           (4, "Barbarrian",  "assaulter",    2,  2,  2,  0,  0,  1)]

### title prof_type, fortitude, reflexes, willpower, spell_resistance, energy_resistance, damage_reduction
c.execute("DROP TABLE IF EXISTS classes")
c.execute("CREATE TABLE classes (\
          'id' INTEGER PRIMARY KEY,\
          'title' TEXT,\
          'prof_type' TEXT, \
          'fort' INTEGER,\
          'ref' INTEGER,\
          'will' INTEGER,\
          's_resist' INTEGER, \
          'e_resist' INTEGER,\
          'dam_reduce' INTEGER);")
c.executemany("INSERT INTO classes VALUES (?,?,?,?,?,?,?,?,?);", (classes))
db.commit()


##--------------------------------------------------------------------
## list of weapons available
### id, weapon_name, weapon_type, damage_type, weapon_damage, weapon_speed, weapon_range, hands):
     
weapons = [(1,  "Fist",                "melee", "bludgeon",    1, 10,   5, 1),
           (2,  "Maul",                "melee", "bludgeon",   10,  1,   5, 2),
           (3,  "WarHammer",           "melee", "bludgeon",    8,  2,   5, 1),
           (4,  "Mace",                "melee", "bludgeon",    6,  3,   5, 1),
           (5,  "Club",                "melee", "bludgeon",    4,  4,   5, 1),
           (6,  "Mallet",              "melee", "bludgeon",    2,  5,   5, 1),
           (7,  "Shillelagh",          "melee", "bludgeon",    2,  6,   5, 1),
           (8,  "GreatSword",          "melee", "slashing",   10,  1,   5, 2),
           (9,  "LongSword",           "melee", "slashing",    8,  3,   5, 1),
           (10, "ShortSword",          "melee", "slashing",    6,  5,   5, 1),
           (11, "LongSpear",           "melee", "peircing",    8,  3,  15, 2),
           (12, "ShortSpear",          "melee", "peircing",    6,  3,  10, 2),
           (13, "Dagger",              "melee", "peircing",    4,  9,   5, 1),
           (14, "GreatAxe",            "melee", "slashing",   10,  1,   5, 2),
           (15, "BattleAxe",           "melee", "slashing",    8,  3,   5, 1),
           (16, "HandAxe",             "melee", "slashing",    4,  5,   5, 1),
           (17, "CompositeLongbow",    "range", "piercing",    8,  5, 100, 2),
           (18, "Longbow",             "range", "piercing",    8,  5,  90, 2),
           (19, "CompositeShortbow",   "range", "piercing",    6,  5,  70, 2),
           (20, "Shortbow",            "range", "piercing",    6,  5,  60, 2),
           (21, "Sling",               "range", "piercing",    3,  5,  30, 2)]
c.execute("DROP TABLE IF EXISTS weapons")
c.execute("CREATE TABLE weapons (\
          'id' INTEGER PRIMARY KEY,\
          'name' TEXT,\
          'type' TEXT, \
          'dam_type' TEXT,\
          'dam' INTEGER,\
          'speed' INTEGER,\
          'range' INTEGER,\
          'hands' INTEGER);")
c.executemany("INSERT INTO weapons VALUES (?,?,?,?,?,?,?,?);", (weapons))
db.commit()


##--------------------------------------------------------------------
## ARMOUR
### id, armour_type, armour_name, armour_protection, armour_weight

armour =  [(1,    "light",    "Padded",           1, 0),
           (2,    "light",    "Leather",          2, 0),
           (3,    "light",    "Studded Leather",  3, 1),
           (4,    "light",    "Chain Shirt",      3, 2),
           (5,    "medium",   "Hide",             4, 2),
           (6,    "medium",   "Scale Mail",       4, 3),
           (7,    "medium",   "Chain Mail",       5, 3),
           (8,    "medium",   "Breastplate",      5, 4),
           (9,    "heavy",    "Splint Mail",      6, 4),
           (10,   "heavy",    "Banded Mail",      6, 5),
           (11,   "heavy",    "Plate Mail",       7, 5),
           (12,   "heavy",    "Half Plate",       7, 6),
           (13,   "heavy",    "Full Plate",       8, 6)]

### id, armour_type, armour_name, armour_protection, armour_weight
c.execute("DROP TABLE IF EXISTS armour")
c.execute("CREATE TABLE armour (\
          'id' INTEGER PRIMARY KEY,\
          'type' TEXT,\
          'name' TEXT,\
          'protection' INTEGER,\
          'weight' INTEGER);")
c.executemany("INSERT INTO armour VALUES (?,?,?,?,?);", (armour))
db.commit()


##--------------------------------------------------------------------
## Shields Available
### id, shield_name, shield_type, deflect, damage_type, bash_damage, attack_speed, attack_range, hands

shields = [(1, "empty",           "light",    0,  "none",     0, 0, 0, 0),
           (2, "Buckler",         "light",    1,  "none",     0, 0, 5, 0),
           (3, "Light Wooden",    "light",    2,  "bludgeon", 1, 2, 5, 1),
           (4, "Light Steel",     "medium",   3,  "bludgeon", 1, 3, 5, 1),
           (5, "Heavy Wooden",    "medium",   4,  "bludgeon", 2, 3, 5, 1),
           (6, "Heavy Steel",     "heavy",    5,  "bludgeon", 2, 4, 5, 1),
           (7, "Tower",           "heavy",    6,  "none",     0, 0, 5, 1)]

###
c.execute("DROP TABLE IF EXISTS shields")
c.execute("CREATE TABLE shields (\
          'id' INTEGER PRIMARY KEY,\
          'name' TEXT,\
          'type' TEXT,\
          'deflect' INTEGER, \
          'dmg_type' TEXT,\
          'bash_dmg' INTEGER,\
          'att_speed' INTEGER,\
          'att_range' INTEGER,\
          'hands' INTEGER);")
c.executemany("INSERT INTO shields VALUES (?,?,?,?,?,?,?,?,?);", (shields))
db.commit()



##--------------------------------------------------------------------
## monsters Available

c.execute("DROP TABLE IF EXISTS characters")
c.execute("CREATE TABLE characters (\
          'id' INTEGER PRIMARY KEY,\
          'name' TEXT, \
          'race' INTEGER, \
          'class' INTEGER, \
          'armour' INTEGER, \
          'lefthand' INTEGER, \
          'righthand' INTEGER, \
          'power' INTEGER, \
          'speed' INTEGER, \
          'level' INTEGER, \
          'total_experience' INTEGER);")
            
characters = []
count = 0
table_id = 0
    

for item in names:
    my_race = random.choice(races)
    my_class = random.choice(classes)
    my_armour = random.choice(armour)
    my_left = random.choice(shields)
    my_right = random.choice(weapons)
    if my_right[7] == 2:
        my_left = shields[0]
    count += 1
    characters.append((count,
                      item,
                      my_race[table_id],
                      my_class[table_id],
                      my_armour[table_id],
                      my_left[table_id],
                      my_right[table_id],
                      0,
                      10,
                      1,
                      0
                      ))

c.executemany("INSERT INTO characters VALUES (?,?,?,?,?,?,?,?,?,?,?);", (characters))
db.commit()



db.close()
