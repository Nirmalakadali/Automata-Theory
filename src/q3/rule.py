from add import *

def rule_func(cell, c, south, north, west, east, southeast, northeast, northwest, southwest):
    if(cell == 0 and (c == 1 or c > 2)):
        return 1
    elif(cell == 1 and (southwest or northwest or west or south or north)):
        return 0
    else:
        return cell
