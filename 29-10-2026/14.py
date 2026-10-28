a = list(map(int, input().split()))
if len(a) > 1:
    a[0], a[-1] = a[-1], a[0]
print(a)
