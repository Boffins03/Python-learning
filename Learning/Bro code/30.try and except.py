try:
    n=int(input("Enter  numinator:"))   
    d=int(input("Enter  denominator:"))
    result=n/d

# except ZeroDivisionError:
#     print("you can't divide any number by zero")  
# except ValueError:
#     print("Enter int value")

except Exception as e:
    print("Some error occur:",e)
else:
    print(result)
finally:
    print("Always work hard")    