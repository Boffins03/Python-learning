cube = lambda x: x*x*x
def fibonacci(n):
    series = [0,1]
    if n == 1:
        series = [0]
        return series
    elif n == 2:
        return series
    elif n == 0:
        series = []
        return  series
    else:
        for _ in range(n-2):
            series.append(series[-1] + series[-2])
        return series

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))