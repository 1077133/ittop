s = input()

letters = 0
digits = 0
spaces = 0
others = 0

for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1
    elif c == " ":
        spaces += 1
    else:
        others += 1

print("Букв:", letters)
print("Цифр:", digits)
print("Пробелов:", spaces)
print("Остальных:", others)
