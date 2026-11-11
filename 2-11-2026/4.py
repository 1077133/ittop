marks = {"Анна": 5, "Иван": 3, "Олег": 4, "Мария": 5, "Пётр": 2}
if marks:
    print("Средняя оценка:", sum(marks.values()) / len(marks))
else:
    print("Нет данных")
count = 0
good_marks = {}
print("Отличники:")
for name, mark in marks.items():
    if mark == 5:
        print(name)
    if mark < 4:
        count += 1
    if mark >= 4:
        good_marks[name] = mark
print("Оценка ниже 4:", count)
print(good_marks)
