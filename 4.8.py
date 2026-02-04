from abc import ABC, abstractmethod
import math

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Автомобіль їде по дорозі")

    def fuel_type(self):
        print("Використовує бензин")

class Bicycle(Vehicle):
    def move(self):
        print("Велосипед рухається педалями")

    def fuel_type(self):
        print("Не потребує пального")

car = Car()
bike = Bicycle()

car.move()
car.fuel_type()

bike.move()
bike.fuel_type()
