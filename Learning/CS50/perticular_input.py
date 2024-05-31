# Getting the int(1-9) input only 
while True:
    try:
        a = int(input("Enter a number under 10:"))
        if a <= 0 or a > 10:
            a = int(input("Enter a number under 10:"))
        else:
            break    
    except:
        continue

        
# Getting the input in string(a-z) only

while True:
    try:
        b = input("Enter a word:").lower()
        if b.isalpha():
            break
        else:
            b = input("Enter a word:").lower()    
    except:
        continue
 