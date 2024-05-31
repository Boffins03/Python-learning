if __name__ == '__main__':
    N = int(input())
    command = []
    value = []
    arr = list()
    for i in range(N):
        a = input().lower().split()
        command.append(a[0])
        if a[0] == "insert":
            temp =[]
            temp.append(a[1])
            temp.append(a[2])
            value.append(temp)
        else:
            if a[0] == "insert" or a[0] == "append" or a[0]== "remove":    
                value.append(a[1])
            else:
                value.append(list())    
        
    
    for j in range(len(command)):
        if command[j] == "append":
            temp = value[j]
            arr.append(int(temp))
        elif command[j] == "insert":
            arr.insert((int(value[j][0])),(int(value[j][1])))
        elif command[j] == "print":
            print(arr)            
        elif command[j] == "reverse":
            arr.reverse()
        elif command[j] == "pop":
            arr.pop()
        elif command[j] == "sort":
            arr.sort()
        elif command[j] == "remove":
            arr.remove(int(value[j]))        