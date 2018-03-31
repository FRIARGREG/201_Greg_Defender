import sqlite3
makefile = "gametest16.sqlite"

class character():
    def __init__(self, verbose = False):
        self.verbose = verbose
        

class makedata():
    def __init__(self, filename, printme = False):
        self.c = None
        self.conn = None
        self.printme = printme
        self.newConnect(filename)
    
    def newConnect(self, sqlite_file):
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()
        if self.printme:
            print("NEW CONNECTION TO FILE: (%s)" % sqlite_file)

    def closeConn(self):
        self.conn.commit()
        if self.printme:
            print("updates have been commited")
        self.conn.close()
        if self.printme:
            print("connection closed")

    def newTable(self, tableName):
        ### create a table
        self.c.execute( "CREATE TABLE %s ('id' INTEGER PRIMARY KEY)" % ( tableName ) )
        self.conn.commit()
        if self.printme:
            print( "TABLE: (%s) CREATED." % tableName )

    def newTableField(self, retrieved):
        table_name, column_name, c_datatype, is_Key = retrieved
        ### add field to table
        ex_string = ("ALTER TABLE %s ADD COLUMN '%s' %s" % (table_name, column_name, c_datatype))
        if is_Key:
            ex_string += " PRIMARY KEY"
        if self.printme:
            print("SQL String = " + ex_string)
        self.c.execute(ex_string)
        self.conn.commit()
        if self.printme and not is_Key:
            print("ADDED FIELD NAME: (%s) TYPE: (%s) TO TABLE: %s" % (column_name, c_datatype, table_name))
        elif self.printme and is_Key:
            print("ADDED FIELD NAME: (%s) TYPE: (%s) AS KEY TO TABLE: %s" % (column_name, c_datatype, table_name))

    def tablePopulate(self, x):
        self.c.executemany('INSERT INTO classes VALUES (?, ?)', (class_data))
        self.conn.commit()
        if printme:
            print("ADDED DATA TO TABLE")

    def new_Character(self):
        self.c.execute("SELECT * INTO TEMP FROM CHARS WHERE 1=2")

    





### LET'S CREATE SOME LISTS OF WHAT WE WANT IN OUR DATABASE

tables = ["cClass", "CHARS", "WEAPONS", "SPELLS", "ARMOURS"]

tablekeys = [
    ("WEAPONS", "id", "INTEGER"),
    ("CHARS", "id", "INTEGER"),
    ("cClass", "id", "INTEGER"),
    ("SPELLS", "id", "INTEGER"),
    ("ARMOURS", "id", "INTEGER")
    ]

tablefields = [
    ("cClass", "name", "TEXT", False),
    ("cClass", "description", "TEXT", False),
    ("cClass", "hd", "INTEGER", False),
    ("CHARS", "name", "TEXT", False),
    ("CHARS", "class", "INTEGER", False),
    ("CHARS", "level", "INTEGER", False),
    ("CHARS", "hp", "INTEGER", False),
    ("WEAPONS", "name", "TEXT", False),
    ("WEAPONS", "description", "TEXT", False),
    ("WEAPONS", "type", "INTEGER", False),
    ("WEAPONS", "dmg_min", "INTEGER", False),
    ("WEAPONS", "dmg_max", "INTEGER", False),
    ("ARMOURS", "name", "TEXT", False),
    ("ARMOURS", "description", "TEXT", False),
    ("ARMOURS", "type", "INTEGER", False),
    ("ARMOURS", "weight", "INTEGER", False),
    ("ARMOURS", "rating", "INTEGER", False),
    ("SPELLS", "name", "TEXT", False),
    ("SPELLS", "description", "TEXT", False),
    ("SPELLS", "type", "INTEGER", False),
    ("SPELLS", "dmg_min", "INTEGER", False),
    ("SPELLS", "dmg_max", "INTEGER", False)
    ]


### NOW LETS MAKE THE DATABASE!!!!


db = makedata(makefile)
db.printme = True

for newtab in tables:
    db.newTable(newtab)

#for newfield in tablekeys:
#    db.newTableField(newfield, True)

for newfield in tablefields:
    db.newTableField(newfield)




### NEXT IS TO POPULATE THE TABLES WITH DATA!!!!
# Larger example that inserts many records at a time
class_data = [
    ]

## class
#id    name     desc      hd
classdata = [
    (1, 'Fighter',  'Good with melee.',         10),
    (2, 'Paladin',  'Destroys Undead.',         10),
    (3, 'Scout',    'Ranged & Wilderness.',     10),
    (4, 'Rogue',    'Sneak and stab.',          6),
    (5, 'Druid',    'Nature magic.',            8),
    (6, 'Wizard',   'Blow em up magic.',        6),
    (7, 'Warlock',  'Raise the Dead.',          6),
    (8, 'Cleric',   'Protective and Healing.',  8)]

## weapons
#ID "name"        "description"                   "type"            "dmg_min"  "dmg_max"
weapondata = [
    (1, 'dagger',       'Small, Sharp, Stabby.',            'PIERCE/RANGE/1',       1, 4),
    (2, 'Short Sword',  'Short, Fast, Accurate.',           'SLASH/MELEE/1',        1, 6),
    (3, 'Long Sword',   'Elegant & Dangerous.',             'SLASH/MELEE/1',        1, 8),
    (4, 'Great Sword',  'Brutal & Slow.',                   'SLASH/MELEE/2',        2, 12),
    (5, 'Club',         'Ug hit puny man!',                 'BLUDGION/MELEE/1',     1, 6),
    (6, 'Mace',         'For letting the divine in.',       'BLUDGION/MELEE/1',     1, 8),
    (7, 'Maul',         'Makes a nice mess of enemies.',    'BLUDGION/MELEE/2',     3, 10),
    (8, 'Battle Pick',  'Pokes holes in armour.',           'PIERCE/MELEE/1',       1, 6),
    (9, 'Battle Axe',   'Removes limbs from bodies.',       'SLASH/MELEE/1',        2, 8),
    (10, 'Spear',       'Hit a target farther away.',       'PIERCE/REACH/2',       2, 12)]

## armours
#ID  "name"            "description"                "type"   "weight"  "rating"
armourdata = [
    (1, 'Padded',           'Material with padding.',       'FLEX',     1, 1),
    (2, 'Leather',          'Boiled skins.',                'FLEX',     2, 3),
    (3, 'Studded Leather',  'Boiled with studs.',           'SEMI',     3, 3),
    (4, 'Chain',            'Links of steel.',              'FLEX',     4, 4),
    (5, 'Scale',            'Tiny scales on leather.',      'SEMI',     4, 5),
    (6, 'Breastplate',      'Steel or hardened leather.',   'RIGID',    5, 5),
    (7, 'Banded',           'Strips of steel.',             'SEMI',     5, 6),
    (8, 'Piece',            'parts of different sets.',     'SEMI',     6, 7),
    (9, 'Plate',            'Large fitted steel shell.',    'RIGID',    8, 8)]

## SPELLS
#ID  "name"            "description"                "type"   "weight"  "rating"
spelldata = [
    (1, 'Fire Bolt',            'Bolt of fire.',                                            'ARCANE', 1, 1),
    (2, 'Ice Bolt',             'Bolt of Ice.',                                             'ARCANE', 2, 3),
    (3, 'Lightning Bolt',       'Bolt of Lightning.',                                       'ARCANE', 3, 3),
    (4, 'Acid Touch',           'Melee touch that burns.',                                  'ARCANE', 4, 4),
    (5, 'Ice Touch',            'Melee touch that freezes.',                                'ARCANE', 4, 5),
    (6, 'Shock Touch',          'Melee touch that shocks.',                                 'ARCANE', 5, 5),
    (7, 'Fire Ball',            'Area that burns.',                                         'ARCANE', 5, 6),
    (8, 'Chain Lightning',      'Area that is shocked.',                                    'ARCANE', 6, 7),
    (9, 'Ice Storm',            'Area that freezes.',                                       'ARCANE', 8, 8),
    (10, 'Find/Know Magic',     'Detects and Identifies Magic spells and Items.',           'ARCANE', 8, 8),
    (11, 'Summon Friend',       'Summon a nearby animal to fight.',                         'NATURE', 8, 8),
    (12, 'Entangle',            'Vines slow enemy movement.',                               'NATURE', 8, 8),
    (13, 'Mud Pool',            'Mud slows movement in area.',                              'NATURE', 8, 8),
    (14, 'Summon Mudman',       'Summon mud creature to fight.',                            'NATURE', 8, 8),
    (15, 'Circle vs Magic',     'Area where magic has less effect.',                        'NATURE', 8, 8),
    (16, 'Summon Treeman',      'Summon wood creature to fight.',                           'NATURE', 8, 8),
    (17, 'Summon Swarm',        'Summon swarm to sting and bite.',                          'NATURE', 8, 8),
    (18, 'Summon Rockman',      'Summon rock creature to fight.',                           'NATURE', 8, 8),
    (19, 'Extreme Weather',     'Area does damage to enemies.',                             'NATURE', 8, 8),
    (20, 'Earthquake',          'Creates fissures, knocks down enemies.',                   'NATURE', 8, 8),
    (21, 'Holy/Unholy Ray',     'Ranged damage vs opposing alignment.',                     'CLERIC', 4, 5),
    (22, 'Heal Living',         'Touched creature gains health.',                           'CLERIC', 5, 5),
    (23, 'Circle vs Arrows',    'Missile weapons do less damage in circle.',                'CLERIC', 8, 8),
    (24, 'Bless',               'Touched creature gains bonus',                             'CLERIC', 8, 8),
    (25, 'Circle vs Elements',  'Fire, Ice, Lightning, Acid do less damage in cirlce.',     'CLERIC', 8, 8),
    (26, 'Guidance',            'See magic and creatures further than sight range.',        'CLERIC', 8, 8),
    (27, 'Circle vs Undead',    'Undead take double damage in circle.',                     'CLERIC', 8, 8),
    (28, 'Heroism',             'Creature touched becomes unafraid.',                       'CLERIC', 8, 8),
    (29, 'Circle vs Good/Evil', 'Opposing alignments take double damage in circle.',        'CLERIC', 8, 8),
    (30, 'Consecrate',          'Undead cannot be healed or raised in area.',               'CLERIC', 8, 8),
    (31, 'Holy/Unholy Ray',     'Ranged damage vs opposing alignment.',                     'WARLOCK', 4, 5),
    (32, 'Animate Skeleton',    'Target corpse becomes skeleton to fight.',                 'WARLOCK', 5, 5),
    (33, 'Steal Life',          'Warlock gains health taken from target living.',           'WARLOCK', 8, 8),
    (34, 'Animate Zombie',      'Target corpse becomes zombie to fight.',                   'WARLOCK', 8, 8),
    (35, 'Whither',             'Target weakens.',                                          'WARLOCK', 8, 8),
    (36, 'Skeleton Horde',      'Area of corpses become skeletons to fight.',               'WARLOCK', 8, 8),
    (37, 'Circle vs Living',    'Living cannot heal and do less damage in circle.',         'WARLOCK', 8, 8),
    (38, 'Zombie Horde',        'Area of corpses become zombies to fight.',                 'WARLOCK', 8, 8),
    (39, 'Desecrate',           'Undead auto-heal and Animates empowered in area.',         'WARLOCK', 8, 8),
    (40, 'Raise Minion',        'Target corpse becomes undead minion of original power.',   'WARLOCK', 8, 8)]




db.c.executemany('INSERT INTO cCLASS VALUES (?,?,?,?)', (classdata))
db.c.executemany('INSERT INTO WEAPONS VALUES (?,?,?,?,?,?)', (weapondata))
db.c.executemany('INSERT INTO ARMOURS VALUES (?,?,?,?,?,?)', (armourdata))
db.c.executemany('INSERT INTO SPELLS VALUES (?,?,?,?,?,?)', (spelldata))


#c.executemany('INSERT INTO characters VALUES (?,?,?,?)', (char_data))




print("completed data update and closing")
db.closeConn()







