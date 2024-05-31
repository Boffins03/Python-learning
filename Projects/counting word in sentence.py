def word_count(phase):
    a=phase.split()
    b={}
    for i in a:
        print(i)
        if i  not in b:
            b[i] = 1
        else:
            b[i] +=1
    return b        

print(word_count("my name is huzaifa and my surname is chauhan"))