def print_rangoli(size):
    # your code goes here
    c = [chr(i) for i in range(ord('a'), ord('z')+1)]
    lines = []
    i = size
    for j in range(i):
        line_chars = []
        for k in range(i-1, j, -1):
            line_chars.append(c[k])
        for k in range(j,i):
            line_chars.append(c[k])     
        line = '-'.join(line_chars) 
        width = (size*2 - 2) + (size*2 - 1)
        lines.append(line.center(width, '-'))   
    for i in range(len(lines)-1):
        lines.insert(i,lines[-(1+i)])
    for i in range(len(lines)):
        print(lines[i])    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)