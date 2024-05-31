class student:
    # making private attribute
    __name = "hello"

    def __init__(self) -> None:
        self.__display()

    def __display(self):
        print(self.__name)
name = student()
