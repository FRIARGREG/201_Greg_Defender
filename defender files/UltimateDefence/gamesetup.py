## This module sets up the game for playing

# 1) first we need to make all the items available

# 2) Then we initiate a character


# 3) Then we set the room and begin play
#   - every action is logged in gamelog.txt
open gamelog.txt for writing
append shit to gamelog.txt


# 4) each room is generated as they are needed.

GenerateRoom()
GenerateMonster()
GenerateTreasure()

# 5) as the character moves, his location is changed in the map
#   - each map square is 5'x5' and all movements will be rounded
#     down to the nearest 5' (cheeky players moving 23' end up moving 20')

initiate map list
