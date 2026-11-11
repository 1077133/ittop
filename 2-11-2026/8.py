student = {
    "id": 101,
    "name": "Анна",
    "age": 18,
    "is_active": True,
    "marks": [5, 4, 5, 4],
    "address": {"city": "Москва", "street": "Лесная"},
    "phone": None
}
print("Имя:", student["name"])
print("Возраст:", student["age"])
print("Город:", student["address"]["city"])
student["marks"].append(5)
student["average"] = sum(student["marks"]) / len(student["marks"])
student["address"]["city"] = "Казань"
student["phone"] = input("Телефон: ")
student["has_scholarship"] = student["is_active"] and student["average"] >= 4.5
for key, value in student.items():
    print(f"{key}: {value}")
