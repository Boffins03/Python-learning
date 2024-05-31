def my_generator():
    yield 1
    yield 3
    yield 5

g = my_generator()

# pirnting the value using next function
value = next(g)
print(value)
value = next(g)
print(value)
value = next(g)
print(value)   

# printing the value using loop
for i in g:
    print(i)