a = list(map(int, input().split()))
for i, x in enumerate(a):
    print(x, i, i - len(a))
