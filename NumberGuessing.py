high = 100000
lo = 0

def Error():
    print("\nthat is not an option from above\n")
    return

def NumberGuesser():
    print('''    \nWelcome to the Number Guesser! If you
    choose to play, this game works by guessing
    the number you are thinking of by asking if
    a number is higher or lower than your number.
    If you choose to simulate, you will give it the
    number you are thinking of and it will tell you
    in how many tries it took to guess your number!''')
    Type = input("\nWould you like to play or simulate? [s/p]\n")
    if Type == "p":
        min, max = lo, high
        Number = input('''\nAlright! Think of any number between '''
        + str(min) + " - " + str(max) + ''' inclusive. 
        Type [done] when you find a number.\n''')
        if Number == "done":
            Play()
        else:
            Error()
    elif Type == "s":
        Simulate()
    else: 
        return
        

def Play():
    min, max = lo, high
    counter = 1
    while True:
        HLE = input("\nis your number higher, lower or equal to " + str((max + min)//2) + " ?" + " [h/l/e]" + "\n")
        if HLE == "h":
            min = (min + max)//2
        elif HLE == "l":
            max = (min + max)//2
        elif HLE == "e":
            print("\nyour number, " + str((max + min)//2) + " was found in " + str(counter) + " tries.\n")
            break
        else:
            Error()
            counter -= 1
        counter += 1

def Simulate():
    min, max = lo, high
    Number2 = input("\nAlright! Think of any number between"
    + str(min) + " - " + str(max) + " inclusive. Type your number below.\n") 
    if int(Number2) > max or int(Number2) < min:
        Error()
        Simulate()
    counter = 1
    while True:
        Number2 = int(Number2)
        if Number2 > (max + min)//2:
            min = (max + min)//2
        elif Number2 < (max + min)//2:
            max = (max + min)//2 
        elif Number2 == (max + min)//2:
            print("\nyour number, " + str((max + min)//2)  + ", was found in " + str(counter) + " tries.\n")
            NumberGuesser()
        counter += 1

while True:
    NumberGuesser()
