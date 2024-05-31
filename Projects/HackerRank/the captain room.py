# Enter your code here. Read input from STDIN. Print output to STDOUT
size_of_group = int(input())
room_number_list = list(map(int,input().split()))
family_room = dict() 
for i in room_number_list:
    if i in family_room.keys():
        family_room[i] += 1
    else:
        family_room[i] = 1

for i in family_room:
    if family_room[i] == 1:
        print(i)            