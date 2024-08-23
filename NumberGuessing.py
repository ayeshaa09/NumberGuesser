
def NumberGuesser():
    max = 100000
    min = 0
    print('''    \nWelcome to the Number Guesser! If you
    choose to play, this game works by guessing
    the number you are thinking of by asking if
    a number is higher or lower than your number.
    If you choose to simulate, you will give it the
    number you are thinking of and it will tell you
    in how many tries it took to guess your number!''')
    Type = input("\nWould you like to play or simulate? [s/p]\n")
    if Type == "p":
        Number = input('''\nAlright! Think of any number between '''
        + str(min) + " - " + str(max) + ''' inclusive. 
        Type [done] when you find a number.\n''')
        if Number == "done":
            HigherOrLowerP()
        else:
            print("that is not one of the options from above.")
            return
    elif Type == "s":
        HigherOrLowerS()
    else: 
        return
        

def HigherOrLowerP():
    max = 100000
    min = 0
    HL = input("\nis your number higher, lower or equal to " + str(max//2) + " ?" + " [h/l/e]" + "\n")
    if HL == "h":
        min = max//2
    elif HL == "l":
        max = max//2
    elif HL == "e":
        print("\nyour number, " + str(max//2) + " was found in 1 try.\n")
        return
    else:
        print("that is not an option from the above")
        HigherOrLowerP()
    counter = 1
    while True:
        counter += 1
        if HL == "h":
            HL2 = input("\nis your number higher, lower or equal to " + str((max + min)//2) + " ?" + " [h/l/e]" + "\n")
            if HL2 == "h":
                min = (max + min)//2
            elif HL2 == "l":
                max = (max + min)//2
            elif HL2 == "e": 
                print("\nyour number, " + str((max + min)//2) + " was found in " + str(counter) + " tries.\n")
                break
            else: 
                print("\nthat is not an option from the above\n")
                continue
            if min == 999:
                min = 1000
        elif HL == "l":
            HL3 = input("\nis your number higher, lower or equal to " + str((max - min)//2 + min) + " ?" + " [h/l/e]" + "\n")
            if HL3 == "h":
                min = (max - min)//2 + min
            elif HL3 == "l":
                max = (max - min)//2 + min
            elif HL3 == "e":
                print("\nyour number, " + str((max + min)//2) + " was found in " + str(counter) + " tries.\n")
                break
            else:
                print("\nthat is not an option from the above\n")
                continue

def HigherOrLowerS():
    max = 100000
    min = 0
    Number2 = input('''\nAlright! Think of any number between '''
    + str(min) + " - " + str(max) + ''' inclusive. 
    Type your number below.\n''') 
    if int(Number2) > max or int(Number2) < min:
        print("\nthat is not an option from the above\n")
        HigherOrLowerS()
    counter = 1
    while True:
        counter += 1
        Number2 = int(Number2)
        if Number2 > (max + min)//2:
            min = (max + min)//2
        elif Number2 < (max - min)//2 + min:
            max = (max - min)//2 + min
        if min == 999:
            min = 1000
        elif Number2 == (max - min)//2 + min:
            print("\nyour number, " + str((max - min)//2 + min) + " was found in " + str(counter) + " tries.\n")
            break
        elif Number2 == (max + min)//2:
            print("\nyour number, " + str((max + min)//2) + " was found in " + str(counter) + " tries.\n")
            break

while True:
    NumberGuesser()
