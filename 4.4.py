class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Студент: {self.name}, Вік: {self.age}, Клас: {self.grade}")

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def show_info(self):
        print(f"Вчитель: {self.name}, Предмет: {self.subject}")

s1 = Student("Іван", 16, 10)
s2 = Student("Олена", 15, 9)
t1 = Teacher("Петро", "Математика")
t2 = Teacher("Марія", "Фізика")

s1.show_info()
s2.show_info()
t1.show_info()
t2.show_info()
