marks = {"Анна": 5, "Иван": 3, "Олег": 4}
print(marks["Иван"])
marks["Иван"] = 4
marks["Мария"] = 5
del marks["Олег"]
print("Количество студентов:", len(marks))
for name, mark in marks.items():
    print(f"{name}: {mark}")
