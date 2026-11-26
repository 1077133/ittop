password = input()
errors = []

if len(password) < 8:
    errors.append("Длина меньше 8 символов")
if not any(c.isupper() for c in password):
    errors.append("Нет заглавной буквы")
if not any(c.islower() for c in password):
    errors.append("Нет строчной буквы")
if not any(c.isdigit() for c in password):
    errors.append("Нет цифры")
if " " in password:
    errors.append("Есть пробелы")

if len(errors) == 0:
    print("Подходит")
else:
    for error in errors:
        print(error)
