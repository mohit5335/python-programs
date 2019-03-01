#program to see the concept of single inheritance in class

class A:
    def __init__(self):
        print("I am in constructor of class A")

    def fun1(self):
        print("I am in class A")

class B(A):                                    #class B is inheriting class A
    def __init__(self):
        super().__init__()                          #calls constructor of class A without creating object of class A
        print("I am in constructor of class B")     #constructor of B called by itself when object of B is created
        
    def fun2(self):
        print("I am in class B")

b = B()    #object of class B

b.fun1()            #b calling fun1()
b.fun2()            #b calling fun2()
