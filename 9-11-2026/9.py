s = input()
result = ""

i = 0
while i < len(s):
    count = 1

    while i + count < len(s) and s[i] == s[i + count]:
        count += 1

    result += s[i] + str(count)
    i += count

print(result)
