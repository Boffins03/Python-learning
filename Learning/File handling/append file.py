import os
file = "myfile2.txt"  # path of the file/directory

if os.path.exists(file):
    with open("myfile2.txt", 'a') as file: # name of the file
        file.write("\nHello, The data is written in the file again.")
        print("Data is appended")
else:
    print("File is not available")