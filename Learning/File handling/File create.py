import os
file = "E:\\Code\\Python\\Learning\\File handling\\myfile2.txt"  # path of the file/directory

if os.path.exists(file):
    print("File is already created")
else:
    with open("E:\\Code\\Python\\Learning\\File handling\\myfile2.txt", 'w'): # name of the file
        print("File Created")