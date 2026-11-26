s = input()
result = ""

for c in s:
    if c not in result:
        result += c

print(result)
