#### this prog is for learning to make new tables from SELECT statements in SQL

import sqlite3
from random import randint

def generateChars(charname, fromscratch = False):
    filename = "gametable.sqlite"
    tablename = 'characters'
    
    db = sqlite3.connect(filename)
    c = db.cursor()


    if fromscratch:
        ## MAKE SURE mytemp TABLE IS DELETED.
        c.execute("DROP TABLE IF EXISTS "+ tablename +";")
        ## CREATE A TEMP TABLE JUST LIKE SPELLS
        c.execute( "CREATE TABLE " + tablename + " (`id` INTEGER, `name` TEXT, `hp` INTEGER, `ac` INTEGER, `wins` INTEGER, `loses` INTEGER, `isDead` INTEGER, PRIMARY KEY(`id`));")
        return "Created table: " + tablename
    else:
        c.execute("SELECT * FROM " + tablename + ";")
        NEWRECORD = len(c.fetchall())
        c.execute("INSERT INTO " + tablename + " VALUES(" + str(NEWRECORD) + ",'"+ charname +"', '" + str(randint(10,25)) + "', '" + str(randint(7,12)) + "', 0, 0, 0);")
        db.commit()
        return "Added Character: " + charname


def printCharacters():
    filename = "gametable.sqlite"
    tablename = 'characters'
    
    db = sqlite3.connect(filename)
    c = db.cursor()

    c.execute("SELECT * FROM "+ tablename +";")
    r = c.fetchall()
    for row in r:
        print(row)




generateChars("", True)

CHARLIST = ["Gregg", "Frani", "Daves", "Sarai", "Leono", "Katet", "Mikeo", 
            "Rheaq", "Crass", "Cruxp", "Hega", "Hogr", "Tina", "Thom", 
            "Jana", "Jorn"]

for name in CHARLIST:
    print("************ Try %s" % name)
    generateChars(name)

printCharacters()

