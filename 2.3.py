students_scores = {
    "Olena": [8, 9, 10],
    "Ivan": [7, 8, 9],
    "Sofia": [10, 10, 9]
}

average_scores = {}
unique_scores = set()

for name, scores in students_scores.items():
    average = sum(scores) / len(scores)
    average_scores[name] = average
    unique_scores.update(scores)

print("Середній бал кожного студента:", average_scores)
print("Унікальні оцінки:", unique_scores)
