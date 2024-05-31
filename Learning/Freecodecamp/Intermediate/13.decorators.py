def my_decorator(func):
    def wrapper():
        print("Start the function")
        func()
        print("End the function")
    return wrapper()

# @my_decorator # we can use this line instead of line 13 
def my_func():
    print("This is my function")


my_func = my_decorator(my_func)
# my_func