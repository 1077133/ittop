a = list(map(int, input().split()))
m = a[0]
for x in a:
    if x > m:
        m = x
print(m)
