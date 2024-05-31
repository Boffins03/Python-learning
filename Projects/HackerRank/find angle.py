# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# Given lengths
AB = float(input())
BC = float(input())
angle_MBC =  round(math.degrees(math.atan(AB/BC)))
print(f"{angle_MBC}\u00b0")


