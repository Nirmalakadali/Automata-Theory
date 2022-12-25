from add import *

def rule_func(cell, c, south, north, west, east, southeast, northeast, northwest, southwest):
    if(cell == 1 and (c == 2 or c == 3)):
        return 1
    elif(cell == 0 and c == 3):
        return 1
    else:
        return 0