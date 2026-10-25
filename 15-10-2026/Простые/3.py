a = list(map(int, input().split()))
k = 0
for x in a:
    if x > 0:
        k += 1
print(k)
