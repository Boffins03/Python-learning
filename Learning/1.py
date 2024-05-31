if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    t=list(student_marks[query_name])
    s=t[0]+t[1]+t[2]
    a=s/3
    print(float(a))
    