def count_substring(string, sub_string):
    l = len(sub_string)
    a = list()    
    for j in range(len(string)):
        print(f"string[{j}:{j+l}] -{string[j:j + l]}")
        a.append(string[j:j + l])
         
    print(a)     
    count = a.count(sub_string)    
    return count

if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)