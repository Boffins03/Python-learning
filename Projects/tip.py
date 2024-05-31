# First program tip
Amount=int(input("Enter the amount:$"))
Tip=int(input("Enter the percent of tip: "))
tip=int((Tip/100)*Amount)
print(f"Amount is {Amount}")
print(f'Tip is {tip}')
sum=Amount + tip
print(f"Total amount is {sum}")
