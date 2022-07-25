import numpy as np
import os
import time

matr = []

#r = int(input("How many Rows? "))
#c = int(input("How many Columns? "))

r = int(input())
c = int(input())

matr = [["." for j in range(c)] for i in range(r)]


#h = int(input("How many are Alive Initially? "))
h = int(input())

for o in range(h):
    #x = int(input(f"What is the x-coordinate of cell {o+1}? "))
    #y = int(input(f"What is the y-coordinate of cell {o+1}? "))
    x = int(input())
    y = int(input())
    matr[x-1][y-1] = "O"

for i in range(r):
    print(' '.join(map(str, matr[i])))

print("_____________")

for l in range(220):

    time.sleep(0.1)
    os.system('clear')
    #print(chr(27)+'[2j')

    left = 0
    right = 0
    up = 0
    down = 0

    copMatr = list(np.copy(matr))

    for i in range(r):
        for j in range(c):
            """currArr = ["." for x in range(c)]
            if (i == 0 and matr[i][j] == "O"):
                left = 1
            if (i == r-1 and matr[i][j] == "O"):
                right = 1
            if (j == 0 and matr[i][j] == "O"):
                up = 1
            if (j == c-1 and matr[i][j] == "O"):
                down = 1"""
                
            numAlive = 0
            numDead = 0

            if (i+1 < r and matr[i+1][j] == "O"): 
                numAlive+=1
            else:
                numDead+=1

            if (j+1 < c and matr[i][j+1] == "O"):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and matr[i-1][j] == "O"):
                numAlive+=1 
            else:
                numDead+=1

            if (j-1 >= 0 and matr[i][j-1] == "O"):
                numAlive+=1 
            else:
                numDead+=1

            if (i+1 < r and j-1 >= 0 and matr[i+1][j-1] == "O"):
                numAlive+=1
            else:
                numDead+=1

            if (i+1 < r and j+1 < c and matr[i+1][j+1] == "O"):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and j-1 >= 0 and matr[i-1][j-1] == "O"):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and j+1 < c and matr[i-1][j+1] == "O"):
                numAlive+=1
            else:
                numDead+=1

            if (matr[i][j] == "." and numAlive == 3):
                copMatr[i][j] = "O"
            elif (matr[i][j] == "O" and (numAlive < 2 or numAlive > 3)):
                copMatr[i][j] = "."

    #if matr == copMatr:
        #break

    for i in range(r):
        print(' '.join(map(str, copMatr[i])))

    print("_____________")
    
    matr = list(np.copy(copMatr))

    """if (left):
        matr.insert(0, currArr)
        r+=1
    if (right):
        matr.insert(r, currArr)
        r+=1
    if (up):
        for i in range(r):
            matr.insert(0, ".")
        c+=1
    if (down):
        for k in range(r):
            matr.append(".")
        c+=1"""

    """for i in range(r):
        print(' '.join(map(str, matr[i])))

    print("_____________")"""
