s = input().lower().replace(" ", "")

if s == s[::-1]:
    print("Да")
else:
    print("Нет")
