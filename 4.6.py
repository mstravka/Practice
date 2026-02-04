class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} видає звук")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} гав-гав!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} мяу-мяу!")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} чірік-чірік!")

dog = Dog("Рекс")
cat = Cat("Мурка")
bird = Bird("Кеша")

dog.speak()
cat.speak()
bird.speak()
