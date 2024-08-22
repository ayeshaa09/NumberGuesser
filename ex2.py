UPPER_LIMIT = 100000
LOWER_LIMIT = 0

def middle(a, b):
    return (a+b)//2

def binarySearch(lo, hi, isHigher):
    mid = middle(lo, hi) 
    if isHigher:
        lo = mid
    else:
        hi = mid
    return lo, hi, middle(lo, hi)

def play():
    print(f"Think of a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
    print("When you are ready to play, say go")
    go = input("> ")
    lo, hi = LOWER_LIMIT, UPPER_LIMIT
    mid = middle(lo, hi)
    tries = 1

    while go == "go":
        if lo == hi:
            print(f"Your number is {lo}!")
        elif lo > hi:
            print("Something went wrong, could not find your number")

        print(f"Is your number higher than or lower than or equal to {mid}? [h/l/e]")
        higherLowerEqual = input("> ")
        if higherLowerEqual == "h":
            higherLowerEqual = True
        elif higherLowerEqual == "l":
            higherLowerEqual = False
        elif higherLowerEqual == "e":
            print(f"Found your number in {tries} tries")
            break
        else:
            break

        lo, hi, mid = binarySearch(lo, hi, higherLowerEqual)
        tries += 1

def simulate():
    print(f"Think of a number between {LOWER_LIMIT} and {UPPER_LIMIT}.")
    print(f"What is your number?")
    number = input("> ")

    if number.isdigit():
        number = int(number)
    else:
        return

    lo, hi = LOWER_LIMIT, UPPER_LIMIT
    mid = middle(lo, hi)
    tries = 1

    while mid != number:
        if lo > hi:
            print("Error: Something went wrong during simulation")
        lo, hi, mid = binarySearch(lo, hi, mid < number)
        tries += 1

    print(f"Found your number in {tries} tries!")
    return


if __name__ == "__main__":
    print("Would you like to play the game or simulate the game? [p/s]")
    playOrSimulate = input("> ")

    if playOrSimulate == "p":
        play()
    elif playOrSimulate == "s":
        simulate()
