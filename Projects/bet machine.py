import math
import random
Max_lines=3
slot1=["Win","Lose","Jackpot"]
slot=[0,1,2]
print("---Welcome to bet machine---")
print("Note:Use only Numbers Please until asked")
def deposit() -> int:
    while True:
        amount=input("Enter the deposit amount:$")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                return amount  
            else:
                amount=input("Enter the amount greater than zero:$")
        else:
            amount=input("Please  enter the deposit amount correctly:$")  
        return amount          

balance=deposit()

def machine(balance):
    balance
    def get_no_of_lines():
        while True:
            lines=input("Enter the number of lines you want to bet on (1-3):")
            if lines.isdigit():
                if lines==0 and lines>Max_lines:
                    lines=input("Enter the no of lines between 1 to 3")
                else:
                    return lines
            else:
                lines=input("Enter the no of lines between 1 to 3")
            return lines    

    def bet_am():
        bet_amount=int(input("Enter the amount you want to bet :$"))
        if bet_amount > balance:
            print("You balance is",balance,"on you can bet !")
            bet_amount=int(input("Enter the amount you want to bet :$"))
        else:
            return bet_amount

    def result():
        if line_bet=='1':
            out1=slot1[random.randint(slot[0],slot[2])]
            print("----",out1,"----")
            if out1=="Win":
                print("Win Your amount is",bet*2)
                amount=bet*2
                return amount  
            elif out1=="Lose":
                print("You loss your bet amount")
                amount=bet*0
                return amount
            elif out1=="Jackpot":
                print("You hit the jackpot.Your amount is",bet*10)
                amount=bet*10
                return amount      
        elif line_bet=='2':
            out1=slot1[random.randint(slot[0],slot[2])]
            out2=slot1[random.randint(slot[0],slot[2])]
            print("----",out1,out2,"----")
            if out1=='Win' and out2=="Win":
                print("Win Your amount is",bet*4)
                amount=bet*4 
                return amount 
            elif out1=="Lose" and out2=="Lose":
                print("You loss your bet amount")
            elif out1=="Jackpot" and out2=="Jackpot":
                print("You hit the jackpot.Your amount is",bet*20)
                amount=bet*20
                return amount
            elif out1=="Win" and out2=="Lose" or out2=="Win" and out1=="Lose":
                print("You lose your bet amount")
                amount=bet*0
                return amount
            elif out1=="Win" and out2=="Jackpot" or out2=="Win" and out1=="Jackpot":
                print("You win.Your amount is",bet*2)
                amount=bet*2
                return amount
            elif out1=="Jackpot" and out2=="Lose" or out2=="Jackpot" and out1=="Lose":
                print("You lose  your bet amount")
                amount=bet*0
                return amount 
        elif line_bet=='3':
            out1=slot1[random.randint(slot[0],slot[2])]
            out3=slot1[random.randint(slot[0],slot[2])]
            out2=slot1[random.randint(slot[0],slot[2])]
            print("----",out1,out2,out3,"----")     
            if out1=='Win' and out2=="Win" and out3=="Win":
                print("Win Your amount is",bet*4)
                amount=bet*10 
                return amount 
            elif out1=="Lose" and out2=="Lose" and out3=="Lose":
                print("You loss your bet amount")
                amount=bet*0
                return amount
            elif out1=="Jackpot" and out2=="Jackpot" and out3=="Jackpot":
                print("You hit the jackpot.Your amount is",bet*100)
                amount=bet*100
                return amount
            elif out1=="Lose" or out2=="Lose" or out3=="Lose":
                print("You lose your bet amount")
                amount=bet*0
                return amount
            elif out1=="Win" and out2=="Jackpot" and out3=="Win" or out2=="Win" and out1=="Jackpot" and out3=="Win" or out1=="Win" and out2=="Win" and out3=="Jackpot":
                print("You win.Your amount is",bet*4)
                amount=bet*4
                return amount

    bet=bet_am()       
    line_bet=get_no_of_lines()
    win_amount=result()
    final_balance=(balance-bet) + win_amount 
    print("Now,Your balance is $",final_balance)
    return final_balance

final_balance=machine(balance)
while final_balance>0:
    a=input("Do you want to play again? yes/no:")
    if a=='yes':
        final_balance=machine(final_balance)
    elif a=='no':
        print("You balance is:$",final_balance)
        break  
    else:
        a=input("Do you want to play again? yes/no:") 
