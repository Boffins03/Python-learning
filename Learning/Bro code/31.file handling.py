import os
import shutil
# #file detection
file="C:\\Users\\Huzaifa Chauhan\\Documents\\Ethical hacking schedule.txt"

if os.path.exists(file):
    print("Exist")
else:
    print("Not Exist")    

#file reading
with open(file) as f:
    print(f.read()) 

# #file write
# text=input("Enter the text you want to enter in the file:")
# with open("write_file.txt","w") as w:
#     w.write(text)
# with open("write_file.txt") as w:    
#     print(w.read())

# #adding new text in file 
# #file write
# text=input("Enter the text you want to enter in the file:",end=" ")
# with open("write_file.txt","a") as w:
#     w.write(text)
# with open("write_file.txt") as w:    
#     print(w.read())

# copy file
# shutil.copyfile("write_file.txt","copyfile.txt")
# shutil.copy("write_file.txt","copy.txt")
# shutil.copy2("write_file.txt","copy2.txt")
# with open("copyfile.txt") as w:    
#     print(w.read())
# with open("copy.txt") as w:    
#     print(w.read())
# with open("copy2.txt") as w:    
#     print(w.read())        

# file move
# try:
#     if os.path.exists(file):
#         print("exist")
#         os.replace("C:\\Users\\Huzaifa Chauhan\\Desktop\\Ethical hacking schedule.txt",file)
#     else:
#         print("don't exist")
# except Exception:
#     print("Some error occur")            

#delete file 
try:
    if os.path.exists("test.txt"):
        os.remove("test.txt")
    else:
        print("file not exist")
except Exception as e:
    print(e,"Error found")

#delete empty_dir
try:
    if os.path.exists("emp_test"):
        os.rmdir("emp_test")
    else:
        print("file not exist")
except Exception as e:
    print(e,"Error found")

#delete dir with file
try:
    if os.path.exists("test"):
        shutil.rmtree("test")
    else:
        print("file not exist")
except Exception as e:
    print(e,"Error found")    
