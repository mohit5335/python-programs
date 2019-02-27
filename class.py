#program to show oops concept in python
class computer:                         #class 

    def __init__(self,cpu,ram):                 #constructor
        self.cpu = cpu
        self.ram = ram
    
    def config(self):                           #method
        print("Config is",self.cpu,self.ram)

c1 = computer('i5',16)          #1st object
c2 = computer('i7',32)          #2nd object

c1.config()         #object calling method
c2.config()

