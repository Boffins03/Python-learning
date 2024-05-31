a = [5,7,4,3,8]
b = len(a)
for i in range(b - 1):
    c = a[i]
    j = i - 1
    while j >= 0 and c < a[j]:
        a[j + 1] = a[j]
        
        j = j - 1
    else:
        a[j + 1] = c
print(a)        
    
