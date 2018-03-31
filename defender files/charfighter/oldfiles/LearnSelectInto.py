#### this prog is for learning to make new tables from SELECT statements in SQL

import sqlite3
from random import randint
filename = "gametest16.sqlite"


db = sqlite3.connect(filename)
## let's see if we can make different things happen with different cursors.
a = db.cursor()
b = db.cursor()
c = db.cursor()



#c.execute("SELECT * INTO temp FROM SPELLS")

## MAKE SURE mytemp TABLE IS DELETED.
c.execute("DROP TABLE IF EXISTS mytemp;")


## CREATE A TEMP TABLE JUST LIKE SPELLS
c.execute( "CREATE TABLE `mytemp` (`id` INTEGER, `name` TEXT, `description` TEXT, `type` TEXT, `dmg_min` INTEGER, `dmg_max` INTEGER, PRIMARY KEY(`id`));")


#c.execute("SELECT * FROM SPELLS WHERE type = 'CLERIC' OR 'NATURE';")
#r = c.fetchall()

#for row in r:
#    print(row)
    #c.execute("INSERT OR IGNORE INTO mytemp VALUES(?,?,?,?,?,?);", row)
#    c.execute("INSERT INTO mytemp VALUES(?,?,?,?,?,?);", row)

c.execute("SELECT * FROM mytemp;")
r = c.fetchall()
for row in r:
    print(row)



def recordMaker():
    b.execute("SELECT * FROM mytemp;")
    NEWRECORD = len(b.fetchall())
    b.execute("INSERT INTO mytemp VALUES(" + str(NEWRECORD) + ",'TEMP','TEMP','TEMP', " + str(randint(1,10)) + ", " + str(randint(15,200)) +");")
    db.commit()

def showtable():
    a.execute("SELECT * FROM mytemp;")
    toprint = a.fetchall()
    for x in toprint:
        print(x)


for x in range(1,25):
    print("************ Try %s" % x)
    recordMaker()
    showtable()

