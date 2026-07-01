#define the parent class to hold general data
class vehicle:
    #the initializer method runs automatically when new objet is created
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    #a method that format and  returns the vehicle details as a string
    def display_info(self):
        return f"{self.brand}({self.year})"
    
#define a child that automatically copy everything from the parent
class car(vehicle):
    pass

#create a new object (Instance) of the class
#then automatically calls the __init__ method from vehicle

my_car = car("BMW", 2026)

#CALLING  the display_info method inherited from the vehical class 
print(my_car.display_info())