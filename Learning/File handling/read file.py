import os
file = "myfile2.txt"  # path of the file/directory

if os.path.exists(file):
    with open("myfile2.txt", 'r') as file: # name of the file
        print(file.read()) # reading whole file
        # reading file line by line
        lines = file.readlines()
        for _ in lines:
            print(_.strip())
else:
    print("File is not available")

 