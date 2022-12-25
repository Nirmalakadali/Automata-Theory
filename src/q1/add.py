from rule import *

import os
import time

with open("q1/config.txt", "r") as f:
    line1 = f.readlines(1)
    rlines = f.readlines()
    for i in line1:
        m = (int)(i.split()[0])
        n = (int)(i.split()[1])
        k = (int)(i.split()[2])

rows = n+2
cols = m+2

count = 0

M = []
for i in range(rows):
    N = []
    for j in range(cols):
        N.append(0)
    M.append(N)

for i in rlines[0:]:
    v1 = i.split()[0]
    v2 = i.split()[1]
    j = (int)(v1)
    k = (int)(v2)
    M[n-k+1][j] = 1

temp = []
for i in range(rows):
    N = []
    for j in range(cols):
        N.append(0)
    temp.append(N)

for i in rlines[0:]:
    v1 = i.split()[0]
    v2 = i.split()[1]
    j = (int)(v1)
    k = (int)(v2)
    temp[n-k+1][j] = 1


def render(M, count):
    os.system("clear")
    print(count)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if(M[i][j] == 0):
                print("O", end="")
            else:
                print("X", end="")
        print()
    time.sleep(0.5)


while(1):

    print("Enter No. of iterations: ")
    t = (int)(input())

    if(t == -1):
        break
    elif(t == 0):
        render(M, count)
        with open("q1/output.txt", "w") as of:
            for i in range(1, rows-1):
                for j in range(1, cols-1):
                    if (M[i][j] == 0):
                        of.write("O")
                    else:
                        of.write("X")
                of.write("\n")
        of.close()

    else:
        while(t):
            # rule
            for i in range(1, rows-1):
                for j in range(1, cols-1):

                    c = 0
                    
                    south = temp[i+1][j]
                    north = temp[i-1][j]
                    west = temp[i][j-1]
                    east = temp[i][j+1]
                    southeast = temp[i+1][j+1]
                    northeast = temp[i-1][j+1]
                    northwest = temp[i-1][j-1]
                    southwest = temp[i+1][j-1]
                    if(north):
                        c += 1
                    if(south):
                        c += 1
                    if(east):
                        c += 1
                    if(west):
                        c += 1
                    if(northeast):
                        c += 1
                    if(southeast):
                        c += 1
                    if(northwest):
                        c += 1
                    if(southwest):
                        c += 1

                    M[i][j] = rule_func(
                        M[i][j], c, south, north, west, east, southeast, northeast, northwest, southwest)

            temp = M

            count = count + 1
            render(M, count)
            t = t-1
            if(t == 0):
                with open("q1/output.txt", "w") as of:
                    for i in range(1, rows-1):
                        for j in range(1, cols-1):
                            if (M[i][j] == 0):
                                of.write("O")
                            else:
                                of.write("X")
                        of.write("\n")
                of.close()
