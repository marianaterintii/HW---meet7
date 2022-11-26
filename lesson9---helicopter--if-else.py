from os import system


system ("cls")
SCALE  = 10

hX = int(input ("lengh coorditantor: "))
hY = int(input ("width coorditantor: "))


map = "" 



############### 1. DRAW MAP #################
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        elif x ==hX -1  and y ==hY:
            map += "~ "
        elif x ==hX -2  and y ==hY:
            map += "~ "
        elif x ==hX +2  and y ==hY:
            map += "~ "
        elif x ==hX +1  and y ==hY:
            map += "~ "
        elif x ==hX +1  and y ==hY -1:
            map += "~ "
        elif x ==hX +2  and y ==hY -1:
            map += "~ "
        elif x ==hX -2  and y ==hY -1:
            map += "~ "
        elif x ==hX -1  and y ==hY -1:
            map += "~ "
        elif x ==hX +1 and y ==hY +1:
            map += "~ "
        elif x ==hX +1 and y ==hY +2:
            map += "~ "
        elif x ==hX +1 and y ==hY -2:
            map += "~ "
        elif x ==hX and y ==hY -2:
            map += "~ "
        elif x ==hX - 1 and y ==hY -2:
            map += "~ "
        elif x ==hX -1 and y == hY +2:
            map += "~ "
        elif x ==hX   and y ==hY -1:
            map += "~ "
        elif x ==hX and y == hY +1:
            map += "~ "
        elif x ==hX and y == hY +2:
            map += "~ "
        elif x ==hX -1 and y == hY +1:
            map += "~ "
        elif x ==hX -2 and y == hY +1:
            map += "~ "
        elif x ==hX +2 and y == hY +1:
            map += "~ "
        else:
            map += "  "
        

       

    map += "\n"   

                     

print(map)

