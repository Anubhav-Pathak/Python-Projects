import sys
from tabulate import tabulate
print("-"*23,"      Tic Tac Toe","-"*23,"    1,1 | 1,2 | 1,3","    "+"-"*16,"    2,1 | 2,2 | 2,3","    "+"-"*16,"    3,1 | 3,2 | 3,3","-"*23, sep="\n")
index = [["-","-","-"],["-","-","-"],["-","-","-"]]
player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")
print("\n----The Game Begins----")
Display = lambda: print(tabulate(index, tablefmt="fancy_grid"))
def Player(chance):
    if chance % 2 != 0: return ("x",player1)
    else: return ("o",player2)
def Input(chance):
    global index
    while True: 
        try:
            x = int(input("Enter the Row: "))
            if x < 0 or x > 3: raise ValueError
            y = int(input("Enter the Column: "))
            if y < 0 or y > 3: raise ValueError
            if x == 0 or y == 0: sys.exit() 
        except ValueError: 
            print("Wrong Input")
            continue
        except KeyboardInterrupt: 
            print("Keyboard Interruption occured")
            continue
        else: 
            if index[x-1][y-1] == "-":
                index[x-1][y-1] = Player(chance)[0]
                return True
            else: print("Place is already filled")
def Win(chance):
    a=b=c=d=0
    ch = Player(chance)[0]
    for i in range(3):
        for j in range(3):
            if index[i][j] == ch: a += 1                #Column
            if index[j][i] == ch: b += 1                #Row
            if i==j and index[i][j] == ch: c += 1       #Left Diagonal
            if i+j==2 and index[i][j] == ch: d += 1     #Right Diagonal
        if a == 3 or b == 3: return True
        a=b=0
    if c == 3 or d == 3: return True        
Display()
for chance in range(1,10):
    print("Chance of",Player(chance)[1])
    Input(chance)
    Display()
    if Win(chance) == True:
        print("\n",Player(chance)[1],"won")
        break
else: print("It's a Draw")