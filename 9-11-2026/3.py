s = input()
k = int(input())

result = ""

for c in s:
    if c == " ":
        result += " "
    else:
        result += chr((ord(c) - ord("a") + k) % 26 + ord("a"))

print(result)
