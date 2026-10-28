a = list(map(int, input().split()))
b = []
c = []
for i in range(len(a)):
    if i % 2 == 0:
        b.append(a[i])
    if a[i] % 2 == 0:
        c.append(a[i])
print(b)
print(c)
