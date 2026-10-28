a = list(map(int, input().split()))
p = n = z = 0
for x in a:
    if x > 0:
        p += 1
    elif x < 0:
        n += 1
    else:
        z += 1
print(p, n, z)
