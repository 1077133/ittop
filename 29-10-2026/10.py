a = list(map(int, input().split()))
s = 0
for x in a:
    s += x
m = s / len(a)
b = []
for x in a:
    if x > m:
        b.append(x)
print(b)
