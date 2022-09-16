import linecache, random, os, sys
def Clear():
    os.system("pause")
    os.system("cls")
def Get(a, b):
    while len(words) < 10:
        line = linecache.getline("Jumble Words.txt", random.randint(a,b))
        word, hint = line.split(": ")
        words[word] = hint
def Jumble(word):
    jumble = list(word)
    random.shuffle(jumble)
    return "".join(jumble)
def Answer(word, hint):
    global c, h, u
    jumble = word
    while jumble == word: jumble = Jumble(word)
    i = 0
    while True:
        answer = input(f"Jumbled word is ' {jumble} ' = ")
        if answer == "x": 
            print("Answer:",word,end="\n\n")
            break
        elif answer == word: 
            print("Correct",end="\n\n")
            c += 1
        elif answer == "?":
            i += 1
            if i == 1 and h < 3: 
                h += 1
                print(f"Hint: {hint}")
            elif i > 1: print("You already used the Hint",end="\n\n")
            else: print("You ran out of Hints",end="\n\n")
            continue
        else: 
            print("Incorrect, Use ? for hint or x to give up",end="\n\n")
            u += 5
            continue
        break
def Generate():
    global c, h, u
    s = list(words)
    i = 0
    while i < 10:
        Answer(s[i],words[s[i]])
        i += 1
    print("-"*45,f"You guessed {c} out of {i} words correctly",f"Hints used: {h}",f"Score: {(c*10)-(h*5)-u}","-"*45,sep="\n")
while True:
    c = h = u = 0
    words = {}
    os.system("clear")
    try: 
        print("-"*26,"       Jumble Words","-"*26,"Press 1 for Easy level","Press 2 for Medium level","Press 3 for Hard Level","Press 4 to exit","-"*26,sep="\n")
        difficulty = int(input("Enter your choice: "))
        if difficulty == 1: Get(1, 30)
        elif difficulty == 2: Get(31,61)
        elif difficulty == 3: Get(62,92)
        elif difficulty == 4: 
            print("Thanks for Playing and have a nice day :)")
            sys.exit()
        else: raise ValueError
        os.system("cls")
        print("---------------------Tutorial--------------------","10 points for Correct Answers","Use ? for Hint, You get 5 points after using Hint","Use x if you dont know the Answer","-5 points for every Incorrect Answers","-"*49,sep="\n")
        Clear()
        Generate()
        Clear()
    except ValueError: 
        print("Wrong Input")
        continue
    except KeyboardInterrupt: 
        print("Keyboard Interruption occured")
        continue
    except FileNotFoundError: 
        print("File not found")
        sys.exit()