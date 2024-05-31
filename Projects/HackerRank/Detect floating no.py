T = int(input())
answer = list()

for _ in range(T):
    N = input()
    if "." in N:
        try:
            N = float(N)
            answer.append(True)
        except:
            answer.append(False)
    else:
        answer.append(False)

for _ in answer:
    print(_)