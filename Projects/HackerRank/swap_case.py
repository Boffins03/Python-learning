def swap_case(s):
    string = list()
    for i in s:
        if i.isupper():
            string.append(i.lower())
        elif i.islower():
            string.append(i.upper())
        else:
            string.append(i)
    my_string = ''.join(map(str, string))
                
    return my_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)