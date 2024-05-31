a = int(input())
answer = list()
for i in range(a):
    try:
        value = input("")
        a,b = value.split()  
        divide = int(a)/int(b)
        answer.append(divide)
    except Exception as e:
        answer.append(f"Error Code:{e}")

for i in answer:
    print(i)

# right answer
a = int(input())
answer = []
for i in range(a):
    try:
        value = input("")
        a, b = value.split()
        divide = int(a) // int(b)
        answer.append(divide)
    except ZeroDivisionError as e:
        answer.append(f"Error Code: {e}")
    except ValueError as e:
        answer.append(f"Error Code: {e}")
    except Exception as e:
        answer.append(f"Error Code: {e}")

for i in answer:
    print(i)
