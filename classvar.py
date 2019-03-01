#in this program we will see types of class variables in python
"""that is the concept of instance variable and static/class variable"""
class car:
    wheels = 4                      #static/class variable
    
    def __init__(self):
        self.milage = 20            #instance varaible
        self.company = 'BMW'        #instance variable

c1 = car()
c2 = car()

c1.milage = 10                  #instance variable changes within the particular instance
c2.company = 'Audi'             #instance variable changes within the particular instance
car.wheels = 2                  #static variable changes within the class

print("c1 Milage = :",c1.milage,"\tc1 Company = :",c1.company,"\tc1 Wheels = :",c1.wheels)
print("c2 Milage = :",c2.milage,"\tc2 Company = :",c2.company,"\tc2 Wheels = :",c2.wheels)
