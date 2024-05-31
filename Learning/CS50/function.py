def main():
    no=int(input("enter a no:"))
    print(hello(no))

def hello(n):
    return n % 2==0

main()

a = input("Enter any thing:").title().strip().split()
print(a)
try:
    b = int(input("enter a no:"))
    def square(b):
        return b ** 2
    print(square(b))
except Exception as error:
        print(error)

