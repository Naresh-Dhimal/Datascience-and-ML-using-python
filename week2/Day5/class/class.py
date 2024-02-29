# class Car:
#     def __init__(self, wheel, doors):
#         self.wheel = wheel
#         self.doors = doors
#         pass
#     def add(self, num1, num2):
#         return num1 + num2, f"wheel = {self.wheel}" 
    
#     def drive(self):
#         print(f"The number of wheel  is {self.wheel}.")
    
# c1 = Car(wheel=7, doors=4)
# c1.drive()


# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        

#     def __init__(self,name, species, age):
#         self.name=name
#         self.species=species
#         self.age = age

        
#     def show(self):
#         print(f'{self.name} is {self.species}')
#         print(self.age)
# a1 = Animal(name='Tiger', species='mammal')
# a1.show()

# class Animal():
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.name = args[0]
#         elif len(args) == 2:
#             self.name = args[0]
#             self.species = args[1]
        
#     def show(self):
#         print(self.name)

# a1 = Animal('cat','cat family')
# a1.show()
#Class Car:
#     pass

# if __name__ == "__main__":
#     car1 = Car()
#     car1.tyres = 4
#     print(car1.tyres)


 # parent_class
class Car():
    def __init__(self,speed):
        self.speed = speed

    def show(self):
        print(self.speed)
        
    #child_class
class Maruti(Car):
    def __init__(self,speed,features):
        self.features = features
        super().__init__(speed)

    def show_featues(self):
        print(self.features)

if __name__ == "__main__":
    c1 = Car(speed=1)
    c1.show()
    c2 = Maruti(speed = 2, features="supra")
    c2.show()
    c2.show_featues()