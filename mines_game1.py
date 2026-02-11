#!/usr/bin/python

r"""
how to run this program and here is sample output of this game

c:\Users\akmis\scratch_feb_7_2026>python mines_game1.py
Mine Game Started
X and Y where you want to move and see what is beneath it
Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
1
Enter y =
1
make next move
total adjacent mines at x = 1 and y = 1 , 0

 score = 1

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
2
Enter y =
1
make next move
total adjacent mines at x = 2 and y = 1 , 2

 score = 2

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
2
Enter y =
2
make next move
total adjacent mines at x = 2 and y = 2 , 2

 score = 3

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
3
Enter y =
3
make next move
total adjacent mines at x = 3 and y = 3 , 3

 score = 4

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
3
Enter y =
3
make next move
total adjacent mines at x = 3 and y = 3 , 3

 score = 5

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
4
Enter y =
4
make next move
total adjacent mines at x = 4 and y = 4 , 3

 score = 6

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
4
Enter y =
5
game over
 score = 6





c:\Users\akmis\scratch_feb_7_2026>python mines_game1.py
Mine Game Started
X and Y where you want to move and see what is beneath it
Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
2
Enter y =
3
make next move
total adjacent mines at x = 2 and y = 3 , 5

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
2
Enter y =
2
make next move
total adjacent mines at x = 2 and y = 2 , 4

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
2
Enter y =
3
make next move
total adjacent mines at x = 2 and y = 3 , 5

Enter  x between 0 and 63
Enter y between 0 and 63
Enter x =
3
Enter y =
3
game over

c:\Users\akmis\scratch_feb_7_2026>
"""








import random
score = 0
MAX_ROWS = 64
MAX_COLUMNS = 64
#initialize the mine list of lists with zeros 
mines =[[0 for x in range(MAX_ROWS)] for y in range(MAX_COLUMNS)] 


previous_row = -1
previous_column = -1


def load_mines(MAX_ROWS,MAX_COLUMNS):
    for i in range(MAX_ROWS):
        for j in range(MAX_COLUMNS):
            if (random.random() >= 0.5):
                mines[i][j] = 1 # one means there is mine at this row column position
            else:
                mines[i][j] = 0 # zero means there is no mine and it is safe to play at this row and column

def get_valid_mine(row,column):
    if (row -1 <= 0):
        row = 0
    if (row + 1 >= MAX_ROWS -1):
        row = MAX_ROWS -1
    if (column - 1 <= 0 ):
        column = 0
    if (column + 1 >= MAX_COLUMNS -1):
        column = MAX_COLUMNS -1
    if (row <= 0):
        row = 0
    if (row >= MAX_ROWS -1):
        row = MAX_ROWS -1
    if (column <= 0):
        column = 0
    if (column >= MAX_COLUMNS -1 ):
        column = MAX_COLUMNS -1
    return mines[row][column]


def adjacent_mines(rows,columns):
    total_adjacent_mines = 0
    for i in -1,0,1:
        for j in -1,0,1:
            if ( i == 0 and j == 0):
                continue;
            elif ( j == 0 and i == 0):
                continue;
            else:
                total_adjacent_mines += get_valid_mine(rows + i,columns + j)
    return total_adjacent_mines


def play_game(row,column):
    global previous_row
    global previous_column
    global score
    if (get_valid_mine(row,column)) == 1:
        print("game over")
        print(" score = %d\n" %(score))
        exit (1)
    else:
        if previous_row != row and previous_column != column:
            print("make next move")
            print("total adjacent mines at x = %d and y = %d , %d\n" %(row,column,adjacent_mines(row,column)))
            previous_row = row
            previous_column = column
            score += 1
        else:
            print("make next move with different x and y then previous move")


if __name__=='__main__':
    load_mines(MAX_ROWS,MAX_COLUMNS)
    
    print("Mine Game Started")
    print("X and Y where you want to move and see what is beneath it ")
    while(1):


        print("Enter  x between 0 and %d" %(MAX_ROWS -1))
        print("Enter y between 0 and %d" %(MAX_COLUMNS -1))
        print("Enter x = ")
        row = int(input())
        print("Enter y = ")
        column = int(input())
        if (row >=0 ) and (row <= MAX_ROWS -1) and (column >= 0) and (column <= MAX_COLUMNS -1):
            play_game(row,column)
            
        else:
            print("invalid input x and/or  y")

        print(" score = %d\n" %(score))
        