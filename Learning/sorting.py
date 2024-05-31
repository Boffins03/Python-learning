a=[5,4,6,8,4,3]
b=len(a)
for i in range(b):
    for j in range(b-1):
        if a[j]>a[j+1]:
           a[j],a[j+1]=a[j+1],a[j]
print(a)        
        
def custom_sort(s):
    # Define a custom sorting key function
    def key_function(c):
        if c.islower():
            return (0, c)
        elif c.isupper():
            return (1, c)
        elif c.isdigit():
            if int(c)%2==0:
                return (3,c)
            else:
                return (2, c)
        else:
            return (4, c)
    
    # Sort the string using the custom key function
    return ''.join(sorted(s, key=key_function))

# Example usage
input_string = "bB4aA3cC2"
sorted_string = custom_sort(input_string)
print(sorted_string)
