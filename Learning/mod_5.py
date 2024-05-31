def closest_higher_mod_5(x)->int:
    remainder = x % 5
    if remainder == 0:
        return x
    else:
        b=0
        while b==x:
            remainder=((x+1) % 5)
            b=x+remainder
            return b
a=closest_higher_mod_5(int(input()))            
print(a)
