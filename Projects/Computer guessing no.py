import random
high = False
def guess(x):
    guess = random.randint(1,x)
    while True:
        try:
            check = computer_guess(x)
        except:
            pass
        if guess > check:
            print("You guess high")
            high = True
            continue
        elif guess < check:
            print("You guess low")
            high = False
            continue
        else:
            print("You guess right")
            break

def computer_guess(x):
    computer_no = random.randint(1,x)
    if high == True:
        computer_no -= 1
        return computer_no
    elif high == False:
        computer_no += 1
        return computer_no

guess(int(input("Enter a no:")))