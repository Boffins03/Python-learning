import random
guess = random.randint(1,10)
while True:
    try:
        check = int(input("Enter the guess no(1-10):"))
    except:
        pass
    if guess == check:
        print("You guess right")
        break
    else:
        pass