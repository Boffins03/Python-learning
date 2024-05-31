import array as ar

arr=ar.array('i',[2,45,90])
print(arr)
arr.append(76)
arr.extend([65,897,564,35])
arr.insert(0,45)
arr.remove(897)
for i in arr:
    print(i)