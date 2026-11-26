n = int(input())
a = [(x, y) for x in range(n + 1) for y in range(x + 1, n + 1)]
print(a)
