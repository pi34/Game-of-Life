matr = []

r = int(input("How many Rows? "))
c = int(input("How many Columns? "))

matr = [[0 for j in range(c)] for i in range(r)]


h = int(input("How many are Alive Initially? "))

for o in range(h):
    x = int(input(f"What is the x-coordinate of cell {o+1}? "))
    y = int(input(f"What is the y-coordinate of cell {o+1}? "))
    matr[x-1][y-1] = 1

for i in range(r):
    print(' '.join(map(str, matr[i])))

print("_____________")

while True:

    left = 0
    right = 0
    up = 0
    down = 0

    copMatr = list(matr)

    for i in range(r):
        for j in range(c):
            currArr = [0 for i in range(c)]
            if (i == 0 and matr[i][j] == 1):
                left = 1
            if (i == r-1 and matr[i][j] == 1):
                right = 1
            if (j == 0 and matr[i][j] == 1):
                up = 1
            if (j == c-1 and matr[i][j] == 1):
                down = 1
                
            numAlive = 0
            numDead = 0

            if (i+1 < r and matr[i+1][j] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (j+1 < c and matr[i][j+1] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and matr[i-1][j] == 1):
                numAlive+=1 
            else:
                numDead+=1

            if (j-1 >= 0 and matr[i][j-1] == 1):
                numAlive+=1 
            else:
                numDead+=1

            if (i+1 < r and j-1 >= 0 and matr[i+1][j-1] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (i+1 < r and j+1 < c and matr[i+1][j+1] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and j-1 >= 0 and matr[i-1][j-1] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (i-1 >= 0 and j+1 < c and matr[i-1][j+1] == 1):
                numAlive+=1
            else:
                numDead+=1

            if (matr[i][j] == 0 and numAlive == 3):
                copMatr[i][j] = 1
            if (matr[i][j] == 1 and (numAlive < 2 or numAlive > 3)):
                copMatr[i][j] = 0

    if matr == copMatr:
        for i in range(r):
            print(' '.join(map(str, matr[i])))

        print("_____________")
        break
    
    matr = list(copMatr)

    if (left):
        matr.insert(0, currArr)
        r+=1
    if (right):
        matr.insert(r, currArr)
        r+=1
    if (up):
        for i in range(r):
            matr.insert(0, 0)
        c+=1
    if (down):
        for k in range(r):
            matr.append(0)
        c+=1

    for i in range(r):
        print(' '.join(map(str, matr[i])))

    print("_____________")
