journal = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4, 3],
    "Олег": [4, 5, 4],
    "Мария": []
}
averages = {}
for name, marks in journal.items():
    if marks:
        averages[name] = sum(marks) / len(marks)
        print(f"{name}: {averages[name]:.2f}")
    else:
        print(f"{name}: нет оценок")
print("Средняя оценка не ниже 4:")
for name, average in averages.items():
    if average >= 4:
        print(f"{name}: {average:.2f}")
if averages:
    best = max(averages.values())
    print("Максимальная средняя оценка:")
    for name, average in averages.items():
        if average == best:
            print(f"{name}: {average:.2f}")
else:
    print("Нет данных")
