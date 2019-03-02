#program to see the concept of multilevel inheritance in class

class A:
    def __init__(self):
        print("I am in constructor of class A")

    def fun1(self):
        print("I am in class A")

class B(A):                                    #class B is inheriting class A
    def __init__(self):                        #calls constructor of A
        super().__init__()                          
        print("I am in constructor of class B")     
        
    def fun2(self):
        print("I am in class B")

class C(B):                                    #class C is inheriting class B
    def __init__(self):
        super().__init__()                     #calls constructor of B    
        print("I am in constructor of class C")     
        
    def fun3(self):
        print("I am in class C")


c = C()         #object of C
c.fun1()        #calls fun1()
c.fun2()        #calls fun2()
c.fun3()        #calls fun3()
