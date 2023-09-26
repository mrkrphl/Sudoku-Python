from random import randrange
from random import choice as randchoice

def printMatrix(table):
    for num in range(0, 81):
        if num % 9 == 0:
            print("")
        if table[num] == 0:
            print('_', end = " ")
        else:
            print(table[num], end = " ")
            
def checkRow(table, pos, num):
    row = int (pos/9)
    start = row*9
    end = start+9
    for val in range(start, end):
        if val == pos: continue
        if table[val] == num:
            return False

    return True

def checkCol(table, pos, num):
    col = (pos % 9)
    start = col
    end = 81 - (9-col)
    for val in range(start, end, 9):
        if val == pos: continue
        if table[val] == num:
            return False

    return True

def checkSubMatrix(table, pos, num):
    #check sub row
    row = int( (int(pos/3)*3))
    start = (row - ((int(row/9))* 9)) + (int(row/27)) * 27
    end = start + 3
    for val in range(start, end):
        if val == pos: continue
        if table[val] == num:
            return False
    start = start + 9
    end = start + 3
    for val in range(start, end):
        if val == pos: continue
        if table[val] == num:
            return False
    start = start + 9
    end = start + 3
    for val in range(start, end):
        if val == pos: continue
        if table[val] == num:
            return False

    return True
              
def checkIfOK(table, pos, num):
    if checkRow(table,pos,num) == False:
          return False
    if checkCol(table,pos,num) == False:

        return False
    if checkSubMatrix(table,pos,num) == False:
        return False
    return True

def solvable(table, pos):
    if pos == 81:
        return True
    if table[pos] == 0:
        for i in range(1,10):
            if checkIfOK(table, pos, i) == True: 
                table[pos] = i
                if solvable(table, pos+1) == False:
                        table[pos] = 0
                else:
                    return True
    else:
        if solvable(table, pos+1) == False:
            return False
        else: return True
    return False

def blankout(table):
    for i in range(0,81):
        chance = randrange(0, 4)
        if chance != 0:
            print('.')
            table[i] = 0
        
def makeTable():
    table = [0]*81
    for i in range(0,int(81 / randrange(2,5))):
        pos = randrange(0, 81)
        num = randrange(1, 10)
        if checkIfOK(table, pos, num) == True:
            table[pos] = num
    return table


solvableTable = [ #for testing
        0, 0, 0, 0, 2, 8, 0, 7, 0,
        0, 0, 0, 3, 0, 0, 0, 0, 8,
        0, 0, 8, 0, 0, 1, 0, 0, 4,
        0, 4, 0, 0, 0, 0, 7, 0, 6,
        0, 8, 0, 7, 5, 6, 0, 4, 0,
        5, 0, 7, 0, 0, 0, 0, 1, 0,
        9, 0, 0, 8, 0, 0, 6, 0, 0,
        8, 0, 0, 0, 0, 9, 0, 0, 0,
        0, 2, 0, 5, 4, 0, 0, 0, 0]

print("This creates a SOLVABLE SUDOKU table\n")
initialTable = makeTable()
print('Initial Table Created')
printMatrix(initialTable)
print('\nInitial Table is Solvable: ', solvable(initialTable, 0))
while(solvable(initialTable, 0) == False):
    print('REMAKING INITIAL TABLE')
    initialTable = makeTable()
    printMatrix(initialTable)
    print('\nInitial Table is Solvable: ', solvable(initialTable, 0))

printMatrix(initialTable)
print('\nBlanking out some cells to solve...')
blankout(initialTable)
print('SUDOKU TABLE TO SOLVE:')
printMatrix(initialTable)
input()



            




    

    
