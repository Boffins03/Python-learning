def print_pattern(n, m):
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

# Example usage:
n, m = map(int, input().split())  # Input format: "n m", where n is the height and m is the width
print_pattern(n, m)
