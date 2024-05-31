#sort list
student=['Don','John','William','Mark']

student.sort()
for i in student:
    print(i)

#sort tuple
student=('Don','John','William','Mark')

sort_student=sorted(student,reverse=True)
for i in sort_student:
    print(i)    

#sort multi list (_name_)
student=[['Don','D',36],
         ['John','B',65],
         ["William","A",89],
         ["Mark",'C',45]]

student.sort()
for i in student:
    print(i)   

#sort multi list (_grade_)
student=[['Don','D',36],
         ['John','B',65],
         ["William","A",89],
         ["Mark",'C',45]]

grade=lambda grade:grade[1]
student.sort(key=grade)
for i in student:
    print(i)  

#sort multi list (_age_)
student=[['Don','D',36],
         ['John','B',65],
         ["William","A",89],
         ["Mark",'C',45]]

age=lambda age:age[2]
student.sort(key=age)
for i in student:
    print(i)      

#sort multi tuple
#sort multi list (_grade_)
student=(('Don','D',36),
         ('John','B',65),
         ("William","A",89),
         ("Mark",'C',45))

grade=lambda grade:grade[1]
student=sorted(student,key=grade)
for i in student:
    print(i)  