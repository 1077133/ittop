phones = {
    "Анна": "+7 900 111-11-11",
    "Иван": "+7 900 222-22-22",
    "Олег": "+7 900 333-33-33"
}
name = input("Имя: ")
if name in phones:
    print(phones[name])
else:
    print("Контакт не найден")
    phones[name] = input("Номер телефона: ")
print("Телефонная книга:")
for name, phone in phones.items():
    print(f"{name}: {phone}")
