# Enter your code here. Read input from STDIN. Print output to STDOUT
def pattern(n, m):
    # Upper Part
    for i in range(n // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

    # Middle Part
    print('WELCOME'.center(m, '-'))

    # Lower Part
    for i in range(n // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(m, '-'))

def main():
    N, M = map(int, input().split())       
    if N%2!=0 and N>5 and N<101:
        if M==3*N and M>15 and M<303:
            pattern(N,M)

if __name__ == "__main__":
    main()