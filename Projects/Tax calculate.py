import math
income=int(input("Enter your income :$"))
percent=0
calculated_tax=0
if income>=0 and income<=15527:
    percent=0
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income>=15528 and income<=42707:
    percent=15
    calculated_tax=math.ceil((percent*income)/100)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
elif income>=42708 and income<=132406:
    percent=25
    calculated_tax=math.ceil((percent*income)/100)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
else:
    percent=28
    calculated_tax=math.ceil((percent*income)/100)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
    
