class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привіт, мене звати {self.name} і мені {self.age} років.")

p1 = Person("Іван", 25)
p2 = Person("Олена", 30)

p1.greet()
p2.greet()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Це автомобіль {self.brand} {self.model}.")

car1 = Car("Toyota", "Corolla")
car2 = Car("BMW", "X5")

car1.info()
car2.info()
