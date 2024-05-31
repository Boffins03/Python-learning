def find_max(number):
    max = number[0]
    for a in number:
        if a > max:
            max = a
    return max
