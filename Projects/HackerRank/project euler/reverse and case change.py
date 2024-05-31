# # #!/bin/python3

# # import math
# # import os
# # import random
# # import re
# # import sys



# # #
# # # Complete the 'reverse_words_order_and_swap_cases' function below.
# # #
# # # The function is expected to return a STRING.
# # # The function accepts STRING sentence as parameter.
# # #

# # def reverse_words_order_and_swap_cases(sentence):
# #     # Write your code here
# #     case = list()
# #     for i in sentence:
# #         if i.upper():
# #             case.append(i.lower())
# #         elif i.lower():
# #             case.append(i.upper())
# #         else:
# #             case.append(i)
# #     print(*case)
                
# # if __name__ == '__main__':
# #     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

# #     sentence = input()

# #     result = reverse_words_order_and_swap_cases(sentence)

# #     # fptr.write(result + '\n')

# #     # fptr.close()

# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys



# #
# # Complete the 'reverse_words_order_and_swap_cases' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING sentence as parameter.
# #

# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     case = list()
#     for i in sentence:
#         print(i)
#         if i.upper():
#             case.append(i.lower())
#         elif i.lower():
#             case.append(i.upper())
#         else:
#             case.append(i)
#     final = list()
#     print(case)
#     for i in range(len(case) -1, 0, -1):
#         final.append(case[i])
#     return "".join(final)
# if __name__ == '__main__':
#     sentence = input()

#     result = reverse_words_order_and_swap_cases(sentence)

#     print(result)

def reverse_words_order_and_swap_cases(sentence):
    # Reverse the order of words and swap cases
    reversed_sentence = ' '.join(word.swapcase() for word in sentence.split()[::-1])
    return reversed_sentence

if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)
