if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Sort the students based on their grades
    students.sort(key=lambda x: x[1])
    
    # Find the second lowest grade
    second_lowest_grade = sorted(list(set(score for name, score in students)))[1]
    
    # Get the names of students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest_grade]
    
    # Sort the names alphabetically
    second_lowest_students.sort()
    
    # Print the names of students with the second lowest grade
    for student in second_lowest_students:
        print(student)