#String
def remove(c):
    r = ""
    seen_char = set()

    for char in c:
        if char not in seen_char:
            r += char
            seen_char.add(char)

    return r
    
    
def merge_the_tools(string, k):
    # your code goes here
    s=string
    a=k
    if len(s)%a==0:
        for i in range(0,len(s),a):
            c=s[i:a+i]
            result=remove(c)
            print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
