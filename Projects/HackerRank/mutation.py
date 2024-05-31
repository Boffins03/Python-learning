def mutate_string(string, position, character):
    string_list = list()
    for i in string:
        string_list.append(i)
        
    string_list[position] = character    
    my_string = ''.join(map(str, string_list))
    return my_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)