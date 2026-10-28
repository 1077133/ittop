a = list(map(int, input().split()))
for i in range(-1, -len(a) - 1, -1):
    print(a[i], end=' ')
print()
for i in range(len(a) - 1, -1, -1):
    print(a[i], end=' ')
print()
i = len(a) - 1
while i >= 0:
    print(a[i], end=' ')
    i -= 1
print()
