
#logic wrapping
from os import system
DIR_UP           = -1
DIR_STOPPED      = 0
DIR_DOWN         = 1

building_roof    = False
building_floors  = 9
buidling_parking = False

lift_floor       = 3
lift_open        = True
lift_dir         = DIR_UP

human_floor      = 3
human_in_lift    = True

############## RENDER FRAME ##########
system ("cls")

if building_roof:
    print ('---|-----|----')
    print (' R |     |    ')

if building_roof == False:
  print (f'---|-----|----')  


for floor in range (9,0,-1):   #(9,8,...,0)

    if floor == lift_floor - 1:
        b = '|---|' 
    else:
        b = '     '
    
    print (f'---|{b}|----')

    if floor == human_floor and not human_in_lift:
        h = ' H  ' 
    else:
        h = '    '
  

    
    if floor == lift_floor + 1:
        if lift_open:
            l = ' < > ' 
        else:
            if lift_dir == DIR_UP:
                 l = ' ^  '
            elif lift_dir == DIR_DOWN:
                l = '    '
            else: 
                l = '     '
    
    else: 
        l = '     '
    
    if floor == lift_floor :
        l = '|   |' 
  
        
    print (f'{floor:^3}|{l}|{h}')



if buidling_parking:
    print ('---|     |----')
    print (' P |     |    ')
    print ('---|-----|----')
else:
    print ('---|-----|----')


############## RENDER FRAME ##########