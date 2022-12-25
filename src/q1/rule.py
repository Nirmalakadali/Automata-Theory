from add import *

def rule_func(cell, c, south, north, west, east, southeast, northeast, northwest, southwest):
    if(east or cell):
        return 1
    else:
        return 0