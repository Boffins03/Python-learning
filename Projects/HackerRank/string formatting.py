def octal(decimal_num,width):
    octal_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num = str(remainder) + octal_num
        decimal_num //= 8
    return octal_num.rjust(width)
    
def hexadecimal(decimal_num,width):
    hexadecimal_digits = "0123456789ABCDEF"
    hexadecimal_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal_num = hexadecimal_digits[remainder] + hexadecimal_num
        decimal_num //= 16
    return hexadecimal_num.rjust(width)

def binary(decimal_num,width):
    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    return binary_num.rjust(width)
        

def print_formatted(number):
    a = len(binary(number,0))
    s = " "
    print(a)
    # your code goes here
    for i in range(1,number+1):
        print(f"{i} {octal(i,a)} {hexadecimal(i,a)} {binary(i,a)}")  

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)