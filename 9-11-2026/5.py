import string

password = input()
errors = []

if len(password) < 8:
    errors.append("Длина меньше 8 символов")
if " " in password:
    errors.append("Пробелы запрещены")
if not any(c in string.ascii_lowercase for c in password):
    errors.append("Нет строчной английской буквы")
if not any(c in string.ascii_uppercase for c in password):
    errors.append("Нет заглавной английской буквы")
if not any(c in string.digits for c in password):
    errors.append("Нет цифры")
if not any(c in string.punctuation for c in password):
    errors.append("Нет знака пунктуации")

if len(errors) == 0:
    print("Подходит")
else:
    for error in errors:
        print(error)
