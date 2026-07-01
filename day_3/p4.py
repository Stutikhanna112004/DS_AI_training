class animal:
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def display_info(self):
        return f"{self.breed}({self.age})"
    
class Dog(animal):
    pass

my_animal = Dog("Baegle", 4)
print(my_animal.display_info())