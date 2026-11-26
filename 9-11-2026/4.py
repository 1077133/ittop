import string

s = input()

letters = 0
digits = 0
punctuation = 0
others = 0

for c in s:
    if c in string.ascii_letters:
        letters += 1
    elif c in string.digits:
        digits += 1
    elif c in string.punctuation:
        punctuation += 1
    else:
        others += 1

print("Букв:", letters)
print("Цифр:", digits)
print("Знаков:", punctuation)
print("Остальных:", others)
