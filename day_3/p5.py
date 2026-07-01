#polymorphism
#parent class
class DietPlan:
    def get_breakfast(self):
        pass
class KetoDiet:
    def get_breakfast(self):
        return "eggs , avacado and chilla"
class VeganDiet(DietPlan):
    def get_breakfast(self):
        return "Oatmeal with milk and chia seeds"
    
class HighprotienDiet(DietPlan):
    def get_breakfast(self):
        return "Greek yougurt with a banana"
    
#polymorphic function
def print_morning_routine(diet_object):
    print(f"Today's Breakfast : {diet_object.get_breakfast()}")

my_keto = KetoDiet()
my_vegan = VeganDiet()
my_protien = HighprotienDiet()

print_morning_routine(my_keto)
print_morning_routine(my_vegan)
print_morning_routine(my_protien)
