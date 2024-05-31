if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    a = list()
    for i in range(len(arr)):
        a.append(int(arr[i]))

    a.sort()
    a = list(set(a))
    print(a[-2])