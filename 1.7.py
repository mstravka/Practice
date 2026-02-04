students = []
n = int(input("Number of students: "))

for _ in range(n):
    name = input("Student name: ")
    grades = []
    for i in range(5):
        grade = int(input(f"Grade {i+1}: "))
        grades.append(grade)
    students.append({"name": name, "grades": grades})

for s in students:
    avg = sum(s["grades"]) / len(s["grades"])
    print(s["name"], "average:", avg)

for i in range(5):
    avg_subject = sum(s["grades"][i] for s in students) / len(students)
    print(f"Subject {i+1} average:", avg_subject)
