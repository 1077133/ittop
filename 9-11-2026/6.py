import string

s = input().lower()
result = ""

for c in string.ascii_lowercase:
    if c not in s:
        result += c

print(result)
