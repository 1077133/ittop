s = input().lower()
result = ""

for c in s:
    if c.isalnum():
        result += c

if result == result[::-1]:
    print("Да")
else:
    print("Нет")
