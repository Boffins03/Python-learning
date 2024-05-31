class family:

    def wakeup(self):
        print("Wakeup")
        return self

    def eat(self):
        print("Eating")
        return self

    def sleep(self):
        print("sleep")
        return self

class father(family):
    def earn(self):
        print("earn")
        return self

class mother(family):
    def cooking(self):
        print("cooking")
        return self     

class child(father,mother):
    def spend(self):
        print("spend")
        return self
    

child().wakeup()\
    .earn().eat().spend().sleep()


def hello():
    print('hello')

hi=hello
hi()
hello()

hi=hello()
hi