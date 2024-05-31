# face_emoji = {
#     "Grinning Face":"😀",
#     "Grinning Face with Big Eyes":"😃",
#     "Grinning Face with Smiling Eyes":"😄",
#     "Beaming Face with Smiling Eyes":"😁",
#     "Grinning Squinting Face":"😆",
#     "Grinning Face with Sweat":"😅",
#     "Face with Tears of Joy":"😂",
#     "Rolling on the Floor Laughing":"🤣",
#     "Smiling Face with Smiling Eyes":"😊",
#     "Smiling Face with Halo":"😇",
#     "Winking Face":"😉",
#     "Heart Eyes":"😍",
#     "Face Blowing a Kiss":"😘",
#     "Face Savoring Food":"😋",
#     "Smiling Face with Sunglasses":"😎",
#     "Smiling Face with Hearts":"🥰",
#     "Neutral Face":"😐",
#     "Expressionless Face":"😑",
#     "Unamused Face":"😒",
#     "Pensive Face":"😔",
#     "Confused Face":"😕"
# }

# # Accessing a specific emoji and its name:
# a=input("Enter the name of emoji:")
# print(f"{a}:{face_emoji[a]}")

# def CodelandUsernameValidation(strParam):
#     has_alpha = any(char.isalpha() for char in strParam)
#     has_digit = any(char.isdigit() for char in strParam)
#     has_underscore = '_' in strParam
   
#     if has_alpha or has_digit or has_underscore :
#       if len(strParam)<4 and len(strParam)>25 or strParam[-1]=="_" or strParam[0]!=has_alpha:
#         return False
#       else:
#         return True
     
# # keep this function call here 
# print(CodelandUsernameValidation(input()))

def fizzBuzz(n):
    if n%3==0 and n%5==0:
        print("FizzBuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")
    else:
        print(n)  

a=15
for i in range(1,a+1):
  fizzBuzz(i)
  
n = int(input())
if n%2==0:
  if n>=2 and n<=5:
    print("Not Weird")
  elif n>=6 and n<=20:
    print("Weird")
  elif n>20:
    print("Not Weird")
else:
  print("Weird")   