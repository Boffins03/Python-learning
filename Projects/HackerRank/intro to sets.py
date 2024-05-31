def average(array):
    # your code goes here
    s = set(array)
    sum = 0
    for i in s:
        sum += i
    return sum/len(s)    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)