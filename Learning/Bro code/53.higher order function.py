# accept function as argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(fun):
    text=fun(input("Enter any text:"))
    print(text)

hello(loud)
hello(quiet)

# return a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide=divisor(2)
print(divide(10))