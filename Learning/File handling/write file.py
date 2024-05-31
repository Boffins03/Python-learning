import os
file = "E:\\Code\\Python\\File handling\\myfile2.txt"  # path of the file/directory

if os.path.exists(file):
    with open("E:\\Code\\Python\\File handling\\myfile2.txt", 'w') as file: # name of the file
        file.write("Hello, The data is written in the file.")
        print("Data is written")
else:
    print("File is not available")